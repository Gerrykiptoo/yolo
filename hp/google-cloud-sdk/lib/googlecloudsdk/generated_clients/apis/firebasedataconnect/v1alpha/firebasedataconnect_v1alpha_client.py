"""Generated client library for firebasedataconnect version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.firebasedataconnect.v1alpha import firebasedataconnect_v1alpha_messages as messages


class FirebasedataconnectV1alpha(base_api.BaseApiClient):
  """Generated client library for service firebasedataconnect version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://firebasedataconnect.googleapis.com/'
  MTLS_BASE_URL = 'https://firebasedataconnect.mtls.googleapis.com/'

  _PACKAGE = 'firebasedataconnect'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'FirebasedataconnectV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new firebasedataconnect handle."""
    url = url or self.BASE_URL
    super(FirebasedataconnectV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_services_connectors = self.ProjectsLocationsServicesConnectorsService(self)
    self.projects_locations_services_schemas = self.ProjectsLocationsServicesSchemasService(self)
    self.projects_locations_services = self.ProjectsLocationsServicesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(FirebasedataconnectV1alpha.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (FirebasedataconnectProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='FirebasedataconnectProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (FirebasedataconnectProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='firebasedataconnect.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (FirebasedataconnectProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (FirebasedataconnectProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsServicesConnectorsService(base_api.BaseApiService):
    """Service class for the projects_locations_services_connectors resource."""

    _NAME = 'projects_locations_services_connectors'

    def __init__(self, client):
      super(FirebasedataconnectV1alpha.ProjectsLocationsServicesConnectorsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Connector in a given project and location. The operations are validated against and must be compatible with the active schema. If the operations and schema are not compatible or if the schema is not present, this will result in an error.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.connectors.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['connectorId', 'requestId', 'validateOnly'],
        relative_path='v1alpha/{+parent}/connectors',
        request_field='connector',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Connector.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors/{connectorsId}',
        http_method='DELETE',
        method_id='firebasedataconnect.projects.locations.services.connectors.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'etag', 'force', 'requestId', 'validateOnly'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def ExecuteMutation(self, request, global_params=None):
      r"""Execute a predefined mutation in a Connector.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsExecuteMutationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ExecuteMutationResponse) The response message.
      """
      config = self.GetMethodConfig('ExecuteMutation')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExecuteMutation.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors/{connectorsId}:executeMutation',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.connectors.executeMutation',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:executeMutation',
        request_field='executeMutationRequest',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsExecuteMutationRequest',
        response_type_name='ExecuteMutationResponse',
        supports_download=False,
    )

    def ExecuteQuery(self, request, global_params=None):
      r"""Execute a predefined query in a Connector.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsExecuteQueryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ExecuteQueryResponse) The response message.
      """
      config = self.GetMethodConfig('ExecuteQuery')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExecuteQuery.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors/{connectorsId}:executeQuery',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.connectors.executeQuery',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:executeQuery',
        request_field='executeQueryRequest',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsExecuteQueryRequest',
        response_type_name='ExecuteQueryResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Connector.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Connector) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors/{connectorsId}',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.services.connectors.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsGetRequest',
        response_type_name='Connector',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Connectors in a given project and location.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectorsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.services.connectors.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/connectors',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsListRequest',
        response_type_name='ListConnectorsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Connector, and creates a new ConnectorRevision with the updated Connector. The operations are validated against and must be compatible with the live schema. If the operations and schema are not compatible or if the schema is not present, this will result in an error.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesConnectorsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/connectors/{connectorsId}',
        http_method='PATCH',
        method_id='firebasedataconnect.projects.locations.services.connectors.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'requestId', 'revisionId', 'updateMask', 'validateOnly'],
        relative_path='v1alpha/{+name}',
        request_field='connector',
        request_type_name='FirebasedataconnectProjectsLocationsServicesConnectorsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsServicesSchemasService(base_api.BaseApiService):
    """Service class for the projects_locations_services_schemas resource."""

    _NAME = 'projects_locations_services_schemas'

    def __init__(self, client):
      super(FirebasedataconnectV1alpha.ProjectsLocationsServicesSchemasService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Schema in a given project and location. Only creation of `schemas/main` is supported and calling create with any other schema ID will result in an error.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesSchemasCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/schemas',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.schemas.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'schemaId', 'validateOnly'],
        relative_path='v1alpha/{+parent}/schemas',
        request_field='schema',
        request_type_name='FirebasedataconnectProjectsLocationsServicesSchemasCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Schema. Because the schema and connectors must be compatible at all times, if this is called while any connectors are active, this will result in an error.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesSchemasDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/schemas/{schemasId}',
        http_method='DELETE',
        method_id='firebasedataconnect.projects.locations.services.schemas.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'etag', 'force', 'requestId', 'validateOnly'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesSchemasDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Schema.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesSchemasGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Schema) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/schemas/{schemasId}',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.services.schemas.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesSchemasGetRequest',
        response_type_name='Schema',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Schemas in a given project and location. Note that only `schemas/main` is supported, so this will always return at most one Schema.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesSchemasListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSchemasResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/schemas',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.services.schemas.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/schemas',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesSchemasListRequest',
        response_type_name='ListSchemasResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Schema, and creates a new SchemaRevision with the updated Schema.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesSchemasPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}/schemas/{schemasId}',
        http_method='PATCH',
        method_id='firebasedataconnect.projects.locations.services.schemas.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'requestId', 'updateMask', 'validateOnly'],
        relative_path='v1alpha/{+name}',
        request_field='schema',
        request_type_name='FirebasedataconnectProjectsLocationsServicesSchemasPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsServicesService(base_api.BaseApiService):
    """Service class for the projects_locations_services resource."""

    _NAME = 'projects_locations_services'

    def __init__(self, client):
      super(FirebasedataconnectV1alpha.ProjectsLocationsServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Service in a given project and location.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'serviceId', 'validateOnly'],
        relative_path='v1alpha/{+parent}/services',
        request_field='service',
        request_type_name='FirebasedataconnectProjectsLocationsServicesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Service.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}',
        http_method='DELETE',
        method_id='firebasedataconnect.projects.locations.services.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'etag', 'force', 'requestId', 'validateOnly'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def ExecuteGraphql(self, request, global_params=None):
      r"""Execute any GraphQL query and mutation against the Firebase Data Connect's generated GraphQL schema. Grants full read and write access to the connected data sources. Note: Use introspection query to explore the generated GraphQL schema.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesExecuteGraphqlRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GraphqlResponse) The response message.
      """
      config = self.GetMethodConfig('ExecuteGraphql')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExecuteGraphql.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}:executeGraphql',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.executeGraphql',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:executeGraphql',
        request_field='graphqlRequest',
        request_type_name='FirebasedataconnectProjectsLocationsServicesExecuteGraphqlRequest',
        response_type_name='GraphqlResponse',
        supports_download=False,
    )

    def ExecuteGraphqlRead(self, request, global_params=None):
      r"""Execute any GraphQL query against the Firebase Data Connect's generated GraphQL schema. Grants full read to the connected data sources. `ExecuteGraphqlRead` is identical to `ExecuteGraphql` except it only accepts read-only query.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesExecuteGraphqlReadRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GraphqlResponse) The response message.
      """
      config = self.GetMethodConfig('ExecuteGraphqlRead')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExecuteGraphqlRead.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}:executeGraphqlRead',
        http_method='POST',
        method_id='firebasedataconnect.projects.locations.services.executeGraphqlRead',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:executeGraphqlRead',
        request_field='graphqlRequest',
        request_type_name='FirebasedataconnectProjectsLocationsServicesExecuteGraphqlReadRequest',
        response_type_name='GraphqlResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Service.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.services.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesGetRequest',
        response_type_name='Service',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Services in a given project and location.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.services.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/services',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsServicesListRequest',
        response_type_name='ListServicesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Service.

      Args:
        request: (FirebasedataconnectProjectsLocationsServicesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/services/{servicesId}',
        http_method='PATCH',
        method_id='firebasedataconnect.projects.locations.services.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['allowMissing', 'requestId', 'updateMask', 'validateOnly'],
        relative_path='v1alpha/{+name}',
        request_field='service',
        request_type_name='FirebasedataconnectProjectsLocationsServicesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(FirebasedataconnectV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (FirebasedataconnectProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (FirebasedataconnectProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations',
        http_method='GET',
        method_id='firebasedataconnect.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='FirebasedataconnectProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(FirebasedataconnectV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
