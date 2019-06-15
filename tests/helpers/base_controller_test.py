import json


class BaseControllerTest:
    """
    Base class for controller tests
    """

    def _build_headers(self, headers=None):
        headers = headers if headers else {}
        return {**{}, **headers}

    def _apply_config_lambdas(self, config):
        out = {}
        for k, v in config.items():
            if k.startswith('$lambda:'):
                out[k.strip('$lambda:')] = eval(v)  # NOT RECOMMENDED BUT IT IS DONE FOR THE SAKE OF FLEXIBILITY
            else:
                out[k] = v
        return out

    def _modify_config(self, app, config):
        config = config if config and isinstance(config, dict) else {}
        config = self._apply_config_lambdas(config)
        app.config = {**app.config, **config}
        return app

    def _make_call(self, method, url, headers, url_parameters, data, query_string, config, app):
        client = app.test_client()
        self._modify_config(app, config)
        headers = self._build_headers(headers=headers)
        url = url.format(**url_parameters) if url_parameters else url
        response = getattr(client, method)(url,
                                           query_string=query_string,
                                           data=json.dumps(data),
                                           headers=headers,
                                           content_type='application/json')
        return response

    def _verify_response(self, expected_response_data, response):
        if expected_response_data and response.status_code != 204:
            assert expected_response_data == json.loads(response.data.decode())

    def _run_standard_test(self, method, url, headers, url_parameters, data, query_string, status_code, response_data,
                           config, app):
        response = self._make_call(method, url, headers, url_parameters, data, query_string, config, app)
        assert status_code == response.status_code
        self._verify_response(response_data, response)
        return response
