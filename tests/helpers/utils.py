import json


def parametrize_from_json_file(
        argnames_str='method, url, headers, url_parameters, data, query_string, status_code,response_data, config',
        fpath='',
        test_class_name='',
        test_class_method=''):
    """
    Function to use in order to populate @pytest.mark.parametrize function from a json file.
    The first level of the json file must contain test_class_name.
    The second level must contain the test_class_method.
    The third level must have (at least) the argnames as keys with the corresponding value to test. Apart from that
    if it has the 'id' field, this will be used to identify the test case

    Note:
        * In order to make it work, unpack the results (see the '**' in the function call)
        * ``argnames_str`` must match the arguments of the test method being parametrize and the key

    Examples:
        >>> @pytest.mark.parametrize(
        >>> **parametrize_from_file(
        >>>     'data,status_code,response_data',
        >>>     current_dir+'/test_cases/test_controller.json',
        >>>     'TestController',
        >>>     'test'
        >>> )

    Args:
        argnames_str (str): ames of the args of the test method separated by comma
        fpath (str): path to the json file containin the parameters of the test
        test_class_name (str): name of the test class which method is being parametrized
        test_class_method (str): name of the method being parametrized

    Returns:
        dict: Pytest parametrize function dictionary
            {
                'argnames': argnames_str,
                'argvalues':(test arguments, list of tuples for the parametrice),
                'ids': ids to identify tests
            }
    """

    argnames = [x.strip() for x in argnames_str.split(',')]
    with open(fpath) as fd:
        data = json.load(fd)
    out = []
    ids = []
    for idx, t in enumerate(data[test_class_name][test_class_method]):
        out.append(tuple(t.get(argname, None) for argname in argnames))
        ids.append(t.get('id', 'test {} '.format(idx)))
    return {'argnames': argnames_str, 'argvalues': out, 'ids': ids}
