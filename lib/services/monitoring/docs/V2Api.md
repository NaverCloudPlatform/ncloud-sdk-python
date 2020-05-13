# ncloud_monitoring.V2Api

All URIs are relative to *https://ncloud.apigw.ntruss.com/monitoring/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_metrics**](V2Api.md#get_list_metrics) | **POST** /getListMetrics | 
[**get_metric_statistics**](V2Api.md#get_metric_statistics) | **POST** /getMetricStatistics | 


# **get_list_metrics**
> GetListMetricsResponse get_list_metrics(get_list_metrics_request)



B.메트릭 리스트 조회

### Example
```python
from __future__ import print_function
import ncloud_monitoring
from ncloud_monitoring.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_monitoring.V2Api(ncloud_monitoring.ApiClient(configuration))
get_list_metrics_request = ncloud_monitoring.GetListMetricsRequest() # GetListMetricsRequest | getListMetricsRequest

try:
    api_response = api_instance.get_list_metrics(get_list_metrics_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_list_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_list_metrics_request** | [**GetListMetricsRequest**](GetListMetricsRequest.md)| getListMetricsRequest | 

### Return type

[**GetListMetricsResponse**](GetListMetricsResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metric_statistics**
> GetMetricStatisticsResponse get_metric_statistics(get_metric_statistics_request)



A.메트릭 통계 조회

### Example
```python
from __future__ import print_function
import ncloud_monitoring
from ncloud_monitoring.rest import ApiException


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.access_key = "YOUR ACCESS KEY"
configuration.secret_key = "YOUR SECRET KEY"
api_instance = ncloud_monitoring.V2Api(ncloud_monitoring.ApiClient(configuration))
get_metric_statistics_request = ncloud_monitoring.GetMetricStatisticsRequest() # GetMetricStatisticsRequest | getMetricStatisticsRequest

try:
    api_response = api_instance.get_metric_statistics(get_metric_statistics_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling V2Api->get_metric_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_metric_statistics_request** | [**GetMetricStatisticsRequest**](GetMetricStatisticsRequest.md)| getMetricStatisticsRequest | 

### Return type

[**GetMetricStatisticsResponse**](GetMetricStatisticsResponse.md)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

