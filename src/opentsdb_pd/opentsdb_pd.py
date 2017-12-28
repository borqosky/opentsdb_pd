import requests
import io

import pandas as pd


def get_timeseries(start, end, metric='', tags='', agg='avg', rate=False, downsample='', hostname='localhost',
                   port=4242, trim=True):

    start_format = start.strftime("%Y/%m/%d-%H:%M:%S")
    end_format = end.strftime("%Y/%m/%d-%H:%M:%S")

    url = 'http://%s:%s/q' % (hostname, port)

    params_name = ['agg', 'downsample', 'rate', 'metric', 'tags']
    params = [agg, downsample, rate, metric, tags]

    _payload = zip(params_name, params)
    payload = dict(
        'm'':'.join(
            ["%s=%s" % (v[0], v[1]) for v in
                filter(lambda x: x[1] is not None, _payload)
             ]
        )
    )

    payload['start'] = start_format
    payload['end'] = end_format

    response = requests.get(url, params=payload)
    response.raise_for_status()

    url_data = response.content
    raw_data = pd.read_csv(io.StringIO(url_data.decode('utf-8')))

    return raw_data
