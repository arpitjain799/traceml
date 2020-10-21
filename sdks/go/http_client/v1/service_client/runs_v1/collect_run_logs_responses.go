// Copyright 2018-2020 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by go-swagger; DO NOT EDIT.

package runs_v1

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"fmt"
	"io"

	"github.com/go-openapi/runtime"
	"github.com/go-openapi/strfmt"

	"github.com/polyaxon/polyaxon/sdks/go/http_client/v1/service_model"
)

// CollectRunLogsReader is a Reader for the CollectRunLogs structure.
type CollectRunLogsReader struct {
	formats strfmt.Registry
}

// ReadResponse reads a server response into the received o.
func (o *CollectRunLogsReader) ReadResponse(response runtime.ClientResponse, consumer runtime.Consumer) (interface{}, error) {
	switch response.Code() {
	case 200:
		result := NewCollectRunLogsOK()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 204:
		result := NewCollectRunLogsNoContent()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return result, nil
	case 403:
		result := NewCollectRunLogsForbidden()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	case 404:
		result := NewCollectRunLogsNotFound()
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		return nil, result
	default:
		result := NewCollectRunLogsDefault(response.Code())
		if err := result.readResponse(response, consumer, o.formats); err != nil {
			return nil, err
		}
		if response.Code()/100 == 2 {
			return result, nil
		}
		return nil, result
	}
}

// NewCollectRunLogsOK creates a CollectRunLogsOK with default headers values
func NewCollectRunLogsOK() *CollectRunLogsOK {
	return &CollectRunLogsOK{}
}

/*CollectRunLogsOK handles this case with default header values.

A successful response.
*/
type CollectRunLogsOK struct {
}

func (o *CollectRunLogsOK) Error() string {
	return fmt.Sprintf("[POST /streams/v1/{namespace}/_internal/{owner}/{project}/runs/{uuid}/{kind}/logs][%d] collectRunLogsOK ", 200)
}

func (o *CollectRunLogsOK) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	return nil
}

// NewCollectRunLogsNoContent creates a CollectRunLogsNoContent with default headers values
func NewCollectRunLogsNoContent() *CollectRunLogsNoContent {
	return &CollectRunLogsNoContent{}
}

/*CollectRunLogsNoContent handles this case with default header values.

No content.
*/
type CollectRunLogsNoContent struct {
	Payload interface{}
}

func (o *CollectRunLogsNoContent) Error() string {
	return fmt.Sprintf("[POST /streams/v1/{namespace}/_internal/{owner}/{project}/runs/{uuid}/{kind}/logs][%d] collectRunLogsNoContent  %+v", 204, o.Payload)
}

func (o *CollectRunLogsNoContent) GetPayload() interface{} {
	return o.Payload
}

func (o *CollectRunLogsNoContent) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCollectRunLogsForbidden creates a CollectRunLogsForbidden with default headers values
func NewCollectRunLogsForbidden() *CollectRunLogsForbidden {
	return &CollectRunLogsForbidden{}
}

/*CollectRunLogsForbidden handles this case with default header values.

You don't have permission to access the resource.
*/
type CollectRunLogsForbidden struct {
	Payload interface{}
}

func (o *CollectRunLogsForbidden) Error() string {
	return fmt.Sprintf("[POST /streams/v1/{namespace}/_internal/{owner}/{project}/runs/{uuid}/{kind}/logs][%d] collectRunLogsForbidden  %+v", 403, o.Payload)
}

func (o *CollectRunLogsForbidden) GetPayload() interface{} {
	return o.Payload
}

func (o *CollectRunLogsForbidden) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCollectRunLogsNotFound creates a CollectRunLogsNotFound with default headers values
func NewCollectRunLogsNotFound() *CollectRunLogsNotFound {
	return &CollectRunLogsNotFound{}
}

/*CollectRunLogsNotFound handles this case with default header values.

Resource does not exist.
*/
type CollectRunLogsNotFound struct {
	Payload interface{}
}

func (o *CollectRunLogsNotFound) Error() string {
	return fmt.Sprintf("[POST /streams/v1/{namespace}/_internal/{owner}/{project}/runs/{uuid}/{kind}/logs][%d] collectRunLogsNotFound  %+v", 404, o.Payload)
}

func (o *CollectRunLogsNotFound) GetPayload() interface{} {
	return o.Payload
}

func (o *CollectRunLogsNotFound) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	// response payload
	if err := consumer.Consume(response.Body(), &o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}

// NewCollectRunLogsDefault creates a CollectRunLogsDefault with default headers values
func NewCollectRunLogsDefault(code int) *CollectRunLogsDefault {
	return &CollectRunLogsDefault{
		_statusCode: code,
	}
}

/*CollectRunLogsDefault handles this case with default header values.

An unexpected error response
*/
type CollectRunLogsDefault struct {
	_statusCode int

	Payload *service_model.RuntimeError
}

// Code gets the status code for the collect run logs default response
func (o *CollectRunLogsDefault) Code() int {
	return o._statusCode
}

func (o *CollectRunLogsDefault) Error() string {
	return fmt.Sprintf("[POST /streams/v1/{namespace}/_internal/{owner}/{project}/runs/{uuid}/{kind}/logs][%d] CollectRunLogs default  %+v", o._statusCode, o.Payload)
}

func (o *CollectRunLogsDefault) GetPayload() *service_model.RuntimeError {
	return o.Payload
}

func (o *CollectRunLogsDefault) readResponse(response runtime.ClientResponse, consumer runtime.Consumer, formats strfmt.Registry) error {

	o.Payload = new(service_model.RuntimeError)

	// response payload
	if err := consumer.Consume(response.Body(), o.Payload); err != nil && err != io.EOF {
		return err
	}

	return nil
}
