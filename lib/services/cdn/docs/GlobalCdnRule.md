# GlobalCdnRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_type_code** | **str** | 프로토콜구분코드 | [optional] 
**service_domain_type_code** | **str** | 서비스도메인구분코드 | [optional] 
**origin_url** | **str** | 원본URL | [optional] 
**origin_path** | **str** | 원본경로 | [optional] 
**origin_http_port** | **int** | 원본HTTP포트 | [optional] 
**origin_https_port** | **int** | 원본HTTPS포트 | [optional] 
**forward_host_header_type_code** | **str** | 포워드호스트헤더구분코드 | [optional] 
**forward_host_header** | **str** | 포워드호스트헤더 | [optional] 
**cache_key_host_name_type_code** | **str** | 캐쉬키호스트명구분코드 | [optional] 
**is_gzip_compression_use** | **bool** | GZIP압축사용여부 | [optional] 
**caching_option_type_code** | **str** | 캐싱옵션구분코드 | [optional] 
**is_error_contents_response_use** | **bool** | 오류내용응답사용여부 | [optional] 
**caching_ttl_time** | **str** | TTL캐싱 | [optional] 
**is_query_string_ignore_use** | **bool** | 쿼리스트링무시여부 | [optional] 
**is_remove_vary_header_use** | **bool** | 헤더제거사용여부 | [optional] 
**is_large_file_optimization_use** | **bool** | 대용량파일최적화사용여부 | [optional] 
**gzip_response_type_code** | **str** | GZIP응답구분코드 | [optional] 
**is_referrer_domain_use** | **bool** | 레퍼러도메인사용여부 | [optional] 
**referrer_domain_list** | **list[str]** | 레퍼러도메인리스트 | [optional] 
**is_referrer_domain_restrict_use** | **bool** | 레퍼러도메인제한사용여부 | [optional] 
**is_secure_token_use** | **bool** | 보안토큰사용여부 | [optional] 
**secure_token_password** | **str** | 보안토큰비밀번호 | [optional] 
**is_reissue_secure_token_password** | **bool** | 보안토큰재발급여부 | [optional] 
**certificate_name** | **str** | 인증서이름 | [optional] 
**is_access_log_use** | **bool** | 엑세스로그사용여부 | [optional] 
**access_log_file_storage_container_name** | **str** | 엑세스로그파일스토리지인스턴스이름 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


