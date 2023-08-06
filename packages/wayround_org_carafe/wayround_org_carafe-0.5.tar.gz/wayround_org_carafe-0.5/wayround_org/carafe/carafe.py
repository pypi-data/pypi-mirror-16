

"""
I was mutch disapointed by BottlePy: Bottle class instances are nailed to
module. So I writed this module
"""

import pprint
import re
import logging
import fnmatch
import urllib.parse
import copy
import mimetypes
import os.path
import time

import wayround_org.utils.path

import wayround_org.http.message

MIME_TEXT = 'text/plain;codepage=UTF-8'
MIME_HTML = 'text/html;codepage=UTF-8'


class Route:

    def __init__(
            self,
            method,
            path_settings,
            target
            ):
        """
        path_settings:
            must be list of 3-tuples. those tuple values have folloving
            meanings:
                0 - path segment matching method: '=', 're', 'rer', 'fm',
                    'path'
                    if this == 'path', this Route (first one found with 'path')
                        will supercide all other Routes for current path
                        segment.
                        Also, if 2 != None, the value in route_result for
                            this - will be list of strings (path splitted by
                            '/'). So if named route_result ends with '', it
                            means what original request target path ends with
                            slash
                1 - pattern. for 0 == 'path' this value is not used.
                        if 0 == 'fm', this value simply a string - file mask
                        if 0 == 're', this value must be compiled regexp, or
                            string which will be compiled into regexp.
                        0 == 'rer' is same as 0 == 're', but instead of string
                            the regular expression result is returned in
                            route_result.
                2 - name (optional. default: None).
                    name frough which resolved value will be available
                    for target. None - if this availability isn't needed

        method: can be any str or list of strs
            None or False - disables matching
            True          - any method accepted

        target - must be callable, which accepts folloving parameters:
            wsgi_environment, response_start - just passed from wsgi server
            route_result - dict (which can be empty) with keys corresponding
                to 2 values in path_settings
        """

        if not callable(target):
            raise TypeError("`target' must be callable")

        if not isinstance(path_settings, list):
            raise TypeError("`path_settings' must be list")

        self.target = target

        if type(method) != list:
            method = [method]

        for i in method:
            if type(i) != str:
                raise ValueError(
                    "invalid value of `method'"
                    )

        for i in range(len(method)):
            method[i] = method[i].strip().upper()

        self.method = method

        if path_settings is None:
            path_settings = [('path', None, 'path')]

        for ii in range(len(path_settings)):
            i = path_settings[ii]

            if not isinstance(i, tuple):
                raise ValueError("`path_settings' values must be tuples")

            len_i = len(i)

            if len_i not in range(2, 4):
                raise ValueError(
                    "`path_settings' list tuples must have 2-3 values each"
                    )

            if len_i == 2:
                path_settings[ii] = (i[0], i[1], None)

        for i in path_settings:
            if not i[0] in ['=', 're', 'rer', 'fm', 'path']:
                raise ValueError(
                    "invalid segment match method: {}".format(i[0])
                    )

        for i in range(len(path_settings) - 1, -1, -1):
            path_settings_i = path_settings[i]

            if (path_settings_i[0] in ['re', 'rer']
                    and type(path_settings_i[1]) == str):

                i2 = (
                    path_settings_i[0],
                    re.compile(path_settings_i[1]),
                    path_settings_i[2]
                    )

                path_settings[i] = i2

        self.path_settings = path_settings

        # TODO: find way to check what all `re' values are compiled

        return

    def __repr__(self):
        ret = []
        for i in self.path_settings:
            ret.append((i[0], i[1]))
        return '{}: {}'.format(super().__repr__(), repr(ret))


def uq(value):
    """
    Shortcut for urllib.parse.unquote
    """
    return urllib.parse.unquote(value)


class Router:

    def __init__(
            self,
            default_target,
            unquote_callable=uq,
            PATH_INFO_mode='std'
            ):
        """
        default_target is same as target in Route class

        by default Router uses uq() function to unquote path segments
        arrived in wsgi_environment['PATH_INFO'] value. you can use
        unquote_callable parameter to override this.

        PATH_INFO_mode parameters is used to switch behavior of PATH_INFO
        treatment. Please, read https://bugs.python.org/issue16679: by
        pep-3333 standard, though it's type is str, it's contents is
        latin-1 and requires additional encoding as latin1 and decoding as
        utf-8. 'std' value here is for standard behavior, and 'unicode' -
        means PATH_INFO value is already unicode string
        """

        if PATH_INFO_mode not in ['std', 'unicode']:
            ValueError("invalid value to `PATH_INFO_mode'")

        if not callable(default_target):
            raise TypeError("`default_target' must be callable")

        self.PATH_INFO_mode = PATH_INFO_mode
        self.routes = []
        self.default_target = default_target
        self.unquote_callable = unquote_callable
        return

    def add(self, method, path_settings, target):
        """
        Simply creates Route and appends it to self.routes

        read Route class docs for parameters meaning
        """
        self.routes.append(Route(method, path_settings, target))
        return

    def add2(self, target, path_settings, method):
        """
        add() with reordered paameters
        """
        return self.add(method, path_settings, target)

    def add3(self, target, path_settings=None, method='GET'):
        """
        add() with reordered paameters
        """
        if path_settings is None:
            path_settings = []
        return self.add(method, path_settings, target)

    def wsgi_server_target(self, wsgi_environment, response_start):
        """
        Searches route in self.routes and passes found target wsgi_environment,
        response_start and route_result. explanation for route_result is in
        Route class.

        result from ranning this method is simply passed from target to carafe
        calling fuctionality. see Carafe class for explanations to this.
        """

        route_result = {}

        request_method = wsgi_environment['REQUEST_METHOD']

        path_info = wsgi_environment['PATH_INFO']

        if self.PATH_INFO_mode == 'std':
            path_info = path_info.encode('latin1').decode('utf-8')
            wsgi_environment['PATH_INFO'] = path_info

        if path_info.startswith('/'):
            path_info = path_info[1:]

        if path_info in ['/', '']:
            splitted_path_info = []
        else:
            splitted_path_info = path_info.split('/')

        for i in range(len(splitted_path_info)):
            splitted_path_info[i] = self.unquote_callable(
                splitted_path_info[i]
                )

        target = self.default_target

        routing_error = False

        # if len(splitted_path_info) != 0 and len(self.routes) != 0:
        if len(self.routes) != 0:

            path_segment_to_check_position = 0

            filter_result = copy.copy(self.routes)

            # filter by method
            for i in range(len(filter_result) - 1, -1, -1):
                filter_result_i = filter_result[i]
                if ((filter_result_i.method in [None, False])
                        or
                        (filter_result_i.method != True
                         and not request_method in filter_result_i.method)):

                    del filter_result[i]

            # filter by path settings
            for i in range(len(splitted_path_info) - 1, -1, -1):

                if len(filter_result) == 0:
                    break

                filter_result = _filter_routes_by_segment(
                    splitted_path_info[i],
                    filter_result,
                    i
                    )

                if (len(filter_result) == 1
                        and filter_result[0].path_settings[i][0] == 'path'):
                    break

            for i in range(len(filter_result) - 1, -1, -1):
                if (len(filter_result[i].path_settings) >
                        len(splitted_path_info)):
                    del filter_result[i]

            selected_route = None

            filter_result_l = len(filter_result)

            if filter_result_l == 0:
                routing_error = True
                logging.error("route not found")

            elif filter_result_l == 1:
                selected_route = filter_result[0]

            else:
                routing_error = True
                logging.error("can't find matching route")

            #print("selected_route 1: {}".format(selected_route))
            #print("route_result 1: {}".format(route_result))

            if selected_route is not None:

                target = selected_route.target

                for i in range(len(selected_route.path_settings)):

                    selected_route_path_settings_i = \
                        selected_route.path_settings[i]

                    if type(selected_route_path_settings_i[2]) == str:

                        selected_route_path_settings_i_0 = \
                            selected_route_path_settings_i[0]

                        selected_route_path_settings_i_2 = \
                            selected_route_path_settings_i[2]

                        if selected_route_path_settings_i_0 == 'path':
                            route_result[selected_route_path_settings_i_2] = \
                                splitted_path_info[i:]
                            break

                        elif selected_route_path_settings_i_0 == '=':
                            route_result[selected_route_path_settings_i_2] = \
                                (selected_route.path_settings[i]
                                 == splitted_path_info[i])

                        elif selected_route_path_settings_i_0 == 'rer':
                            route_result[selected_route_path_settings_i_2] = \
                                selected_route.path_settings[i].match(
                                    splitted_path_info[i]
                                    )

                        elif selected_route_path_settings_i_0 in ['fm', 're']:
                            route_result[selected_route_path_settings_i_2] = \
                                splitted_path_info[i]

                        else:
                            raise Exception("programming error")

            #print("route_result 2: {}".format(route_result))

        if routing_error:
            logging.error(
                "routing error\n"
                "   asked route is: {}\n"
                "   starting  route list is: {}\n"
                "   resulting route list is: {}".format(
                    path_info,
                    self.routes,
                    filter_result
                    )
                )

        if len(self.routes) == 0:
            logging.warning("routes not specified")

        return target(wsgi_environment, response_start, route_result)


def _filter_routes_by_segment(
        actual_segment_value,
        routes_lst,
        routes_segment_index
        ):

    _debug = False

    if _debug:
        print("""
_filter_routes_by_segment(
    {},
    {},
    {}
    )""".format(
            actual_segment_value,
            routes_lst,
            routes_segment_index
            )
        )

    ret = copy.copy(routes_lst)

    true_path_found_atonce = False
    for i in ret:

        if routes_segment_index > len(i.path_settings) - 1:
            continue

        if i.path_settings[routes_segment_index][0] == 'path':
            true_path_found_atonce = True
            ret = [i]
            break

    if not true_path_found_atonce:

        for i in range(len(ret) - 1, -1, -1):
            ii = ret[i]

            if routes_segment_index > len(ii.path_settings) - 1:
                del ret[i]

        for i in range(len(ret) - 1, -1, -1):
            ii = ret[i]

            match = False
            meth = ii.path_settings[routes_segment_index][0]
            if meth == 're':
                if ii.path_settings[routes_segment_index][1].match(
                        actual_segment_value
                        ):
                    match = True
            elif meth == 'fm':
                if fnmatch.fnmatch(
                        actual_segment_value,
                        ii.path_settings[routes_segment_index][1]
                        ):
                    match = True
            elif meth == 'path':
                match = True
            elif meth == '=':
                match = (
                    ii.path_settings[routes_segment_index][1]
                    == actual_segment_value
                    )
            else:
                raise Exception("programming error: invalid method value")

            if not match:
                del ret[i]

    if _debug:
        print("_filter_routes_by_segment result: {}".format(ret))

    return ret


class _EnvironWSGIHandler:

    def __init__(self, environ_handler):
        if not isinstance(environ_handler, EnvironHandler):
            raise TypeError("invalid type")
        self._environ_handler = environ_handler
        return

    @property
    def version(self):
        return self._environ_handler['wsgi.version']

    @property
    def url_scheme(self):
        return self._environ_handler['wsgi.url_scheme']

    @property
    def input(self):
        return self._environ_handler['wsgi.input']

    @property
    def errors(self):
        return self._environ_handler['wsgi.errors']

    @property
    def multithread(self):
        return self._environ_handler['wsgi.multithread']

    @property
    def multiprocess(self):
        return self._environ_handler['wsgi.multiprocess']

    @property
    def run_once(self):
        return self._environ_handler['wsgi.run_once']


class EnvironHandler:

    def __init__(self, environ, encoding='utf-8'):
        if not isinstance(environ, dict):
            raise TypeError("`environ' must be dict")
        self._environ = environ
        self._encoding = encoding
        self.wsgi = _EnvironWSGIHandler(self)
        return

    def get_original(self):
        return self._environ

    def __getitem__(self, key):
        return self._environ.get(key, None)

    def __setitem__(self, key, value):
        if key not in ['PATH_INFO']:
            raise KeyError("invalid key")

        self._environ[key] = value
        return

    def __len__(self):
        return len(self._environ)

    def __repr__(self):
        return pprint.pformat(self._environ)

    def __str__(self):
        return str(self._environ)

    @property
    def request_method(self):
        return self['REQUEST_METHOD']

    @property
    def script_name(self):
        return self['SCRIPT_NAME']

    @property
    def path_info(self):
        return self['PATH_INFO']

    @path_info.setter
    def path_info(self, value):
        # TODO: do we need value checks?
        self._environ['PATH_INFO'] = value
        return

    def get_path_info_splitted(self):
        return wayround_org.utils.path.split(self.path_info)

    @property
    def query_string(self):
        return self['QUERY_STRING']

    def parse_qs(self, *args, **kwargs):
        return urllib.parse.parse_qs(
            self.query_string,
            *args,
            **kwargs
            )

    def parse_qsl(self, *args, **kwargs):
        return urllib.parse.parse_qsl(
            self.query_string,
            *args,
            **kwargs
            )

    @property
    def content_type(self):
        return self['CONTENT_TYPE']

    @property
    def content_length(self):
        return self['CONTENT_LENGTH']

    @property
    def server_name(self):
        return self['SERVER_NAME']

    @property
    def server_port(self):
        return self['SERVER_PORT']

    @property
    def server_protocol(self):
        return self['SERVER_PROTOCOL']


class CarafeIterableIterator:

    def __init__(self, iterator, output_encoding='utf-8'):
        self._iterator = iterator
        self._stop_flag = False
        self.output_encoding = output_encoding
        return

    def __iter__(self):
        for i in self._iterator.__iter__():

            if self._stop_flag:
                if hasattr(self._iterator, 'stop'):
                    getattr(self._iterator, 'stop')()
                    break

            i_t = type(i)

            i_r = None

            if i_t == bytes:
                i_r = res

            elif i_t == str:
                i_r = bytes(res, self.output_encoding)

            else:
                raise TypeError(
                    "iterator `{}' returned invalid value".format(
                        self._iterator
                        )
                    )

            yield i_r

        return

    def stop(self):
        self._stop_flag = True
        return


class ResponseStartWrapper:

    """
    Wrapper for response_start function provided by WSGI server

    It transparantly converts strs to bytes

    This callable wrapper is mimics standard WSGI response_start callable,
    but adds some incompatible things:
        * status (in distinct to WSGI, where it must be str with code and
          reason) can be just int or string with code but without reason.
          in such a case, the reason is taken from Python standard
          http.client.responses dictionary
    """

    def __init__(self, response_start, output_encoding='utf-8'):
        self._response_start = response_start
        self._output_encoding = output_encoding
        return

    def __call__(self, status, response_headers=None, exc_info=None):

        if response_headers is None:
            response_headers = [('Content-Type', MIME_TEXT)]

        response_headers_error_msg = \
            "`response_headers' must be a list of 2 tuples"

        if not isinstance(response_headers, list):
            raise Exception(response_headers_error_msg)
        else:
            for i in response_headers:
                if not len(i) == 2:
                    raise Exception(response_headers_error_msg)

        if type(status) == int:
            status = str(status)

        status_code = None
        status_reason = None

        status_splitted = status.strip().split(' ')

        status_splitted_l = len(status_splitted)

        if status_splitted_l not in range(1, 3):
            raise ValueError("Invalid `status' value")

        status_code = int(status_splitted[0])

        if status_splitted_l > 1:
            status_reason = status_splitted[1]

        status_format_res = wayround_org.http.message.format_status(
            status_code,
            status_reason
            )

        return ResponseStartResultWrapper(
            self._response_start(
                status_format_res,
                response_headers,
                exc_info
                ),
            self._output_encoding
            )


class ResponseStartResultWrapper:

    def __init__(self, response_start_result, output_encoding='utf-8'):
        self._response_start_result = response_start_result
        self._output_encoding = output_encoding
        return

    def __call__(self, data):
        raise Exception("This data return method is deprecated. Don't use it!")
        if isinstance(data, str):
            data = bytes(data, self._output_encoding)
        return self._response_start_result(data)


class Carafe:

    def __init__(self, carafe_app, output_encoding='utf-8'):
        """
        carafe_app - must be callable which has
            (wsgi_environment, response_start) parameters.

            wsgi_environment - is wrapped with EnvironHandler class, which does
                not do any changes to dictionary, but only provides handy
                attributes. moreover EnvironHandler behaves like a mapping
                object. original dict is returned with get_original() method if
                needed.

            response_start - is wrapped with special class, which, when called,
                raises exception as deprecation mesure

            carafe_app must return bytes, str, list of bytes or strs, or
            iterable. if iterable is returned, it is converted with other
            internal iterable which is converts returned strs into bytes.
        """
        self.carafe_app = carafe_app
        self.output_encoding = output_encoding
        return

    def target_for_wsgi_server(self, wsgi_environment, response_start):

        ret = None

        try:
            res = self.carafe_app(
                EnvironHandler(wsgi_environment, self.output_encoding),
                ResponseStartWrapper(response_start)
                )

        except Exception as e:
            # TODO: check status correctness
            response_start('500 Error', [], e)
            ret = [b'Internal Server Error']
            logging.exception("Error calling `{}'".format(self.carafe_app))
        else:

            if res is None:
                res = []

            res_t = type(res)

            if res_t == bytes:
                ret = [res]

            elif res_t == str:
                ret = [bytes(res, self.output_encoding)]

            elif res_t == list:
                ret = []
                for i in res:
                    i_t = type(i)
                    if i_t == bytes:
                        ret.append(i)

                    elif i_t == str:
                        ret.append(bytes(i, self.output_encoding))

                    else:
                        raise ValueError(
                            "if list is returned it bust contain strs or bytes"
                            )
            elif hasattr(res, '__iter__'):
                if not callable(res):
                    raise ValueError("invalid iterator returned")

                if hasattr(res, 'stop'):
                    if not callable(getattr(res, 'stop')):
                        raise Exception(
                            "returned iteratable has invalid 'stop' method"
                            )

                ret = CarafeIterableIterator(res_iter, self.output_encoding)

            else:
                raise TypeError("some invalid data type returned")

        return ret


def static_file(
        start_response_cb,
        filename,
        root,
        mimetype='auto',
        download=False,
        charset='UTF-8'
        ):
    """
    Note: this function is simply an adopted and fixed copy&paste from
          bottle.py cause I'm too lazy to reinvent this wheel.

    Open a file in a safe way and return :exc:`HTTPResponse` with status
    code 200, 305, 403 or 404. The ``Content-Type``, ``Content-Encoding``,
    ``Content-Length`` and ``Last-Modified`` headers are set if possible.
    Special support for ``If-Modified-Since``, ``Range`` and ``HEAD``
    requests.

    :param filename: Name or path of the file to send.
    :param root: Root path for file lookups. Should be an absolute directory
        path.
    :param mimetype: Defines the content-type header (default: guess from
        file extension)
    :param download: If True, ask the browser to open a `Save as...` dialog
        instead of opening the file with the associated program. You can
        specify a custom filename as a string. If not specified, the
        original filename is used (default: False).
    :param charset: The charset to use for files with a ``text/*``
        mime-type. (default: UTF-8)
    """

    # TODO: this function coding is disaster. need to rewrite.

    root = wayround_org.utils.path.realpath(root) + os.sep
    filename = wayround_org.utils.path.realpath(
        wayround_org.utils.path.join(
            root,
            filename
            )
        )

    headers = dict()

    if not filename.startswith(root):
        return wayround_org.http.message.HTTPError(
            403,
            "Access denied"
            )

    if not os.path.exists(filename) or not os.path.isfile(filename):
        return wayround_org.http.message.HTTPError(
            404,
            "File does not exist"
            )

    if not os.access(filename, os.R_OK):
        return wayround_org.http.message.HTTPError(
            403,
            "You do not have permission to access this file"
            )

    if mimetype == 'auto':
        mimetype, encoding = mimetypes.guess_type(filename)
        if encoding:
            headers['Content-Encoding'] = encoding

    if mimetype:
        if (
                mimetype.startswith('text/')
                and charset
                and 'charset' not in mimetype
                ):

            mimetype += '; charset={}'.format(charset)

        headers['Content-Type'] = mimetype

    if download:
        download = os.path.basename(filename if download == True else download)
        headers['Content-Disposition'] = 'attachment; filename="{}"'.format(
            download
            )

    stats = os.stat(filename)
    headers['Content-Length'] = clen = stats.st_size
    lm = time.strftime(
        "%a, %d %b %Y %H:%M:%S GMT",
        time.gmtime(
            stats.st_mtime
            )
        )
    headers['Last-Modified'] = lm

    ims = request.environ.get('HTTP_IF_MODIFIED_SINCE')

    if ims:
        ims = parse_date(ims.split(";")[0].strip())

    if ims is not None and ims >= int(stats.st_mtime):
        headers['Date'] = time.strftime(
            "%a, %d %b %Y %H:%M:%S GMT",
            time.gmtime()
            )
        start_response_cb(304, headers)
        return HTTPResponse(304, **headers)

    body = '' if request.method == 'HEAD' else open(filename, 'rb')

    headers["Accept-Ranges"] = "bytes"
    ranges = request.environ.get('HTTP_RANGE')
    if 'HTTP_RANGE' in request.environ:
        ranges = list(
            parse_range_header(
                request.environ['HTTP_RANGE'],
                clen
                )
            )

        if not ranges:
            return wayround_org.http.message.HTTPError(
                416,
                "Requested Range Not Satisfiable"
                )

        offset, end = ranges[0]
        headers["Content-Range"] = "bytes %d-%d/%d" % (offset, end - 1, clen)
        headers["Content-Length"] = str(end - offset)

        if body:
            body = _file_iter_range(body, offset, end - offset)

        return wayround_org.http.message.HTTPResponse(
            206,
            headers,
            body
            )

    return wayround_org.http.message.HTTPResponse(200, headers, body)
