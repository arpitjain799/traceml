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

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.2.1-rc1
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.V1EventCurveKind;

/**
 * V1EventCurve
 */

public class V1EventCurve {
  public static final String SERIALIZED_NAME_KIND = "kind";
  @SerializedName(SERIALIZED_NAME_KIND)
  private V1EventCurveKind kind = V1EventCurveKind.ROC;

  public static final String SERIALIZED_NAME_X = "x";
  @SerializedName(SERIALIZED_NAME_X)
  private List<Float> x = null;

  public static final String SERIALIZED_NAME_Y = "y";
  @SerializedName(SERIALIZED_NAME_Y)
  private List<Float> y = null;

  public static final String SERIALIZED_NAME_ANNOTATION = "annotation";
  @SerializedName(SERIALIZED_NAME_ANNOTATION)
  private String annotation;


  public V1EventCurve kind(V1EventCurveKind kind) {
    
    this.kind = kind;
    return this;
  }

   /**
   * Get kind
   * @return kind
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1EventCurveKind getKind() {
    return kind;
  }


  public void setKind(V1EventCurveKind kind) {
    this.kind = kind;
  }


  public V1EventCurve x(List<Float> x) {
    
    this.x = x;
    return this;
  }

  public V1EventCurve addXItem(Float xItem) {
    if (this.x == null) {
      this.x = new ArrayList<Float>();
    }
    this.x.add(xItem);
    return this;
  }

   /**
   * Get x
   * @return x
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<Float> getX() {
    return x;
  }


  public void setX(List<Float> x) {
    this.x = x;
  }


  public V1EventCurve y(List<Float> y) {
    
    this.y = y;
    return this;
  }

  public V1EventCurve addYItem(Float yItem) {
    if (this.y == null) {
      this.y = new ArrayList<Float>();
    }
    this.y.add(yItem);
    return this;
  }

   /**
   * Get y
   * @return y
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<Float> getY() {
    return y;
  }


  public void setY(List<Float> y) {
    this.y = y;
  }


  public V1EventCurve annotation(String annotation) {
    
    this.annotation = annotation;
    return this;
  }

   /**
   * Get annotation
   * @return annotation
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAnnotation() {
    return annotation;
  }


  public void setAnnotation(String annotation) {
    this.annotation = annotation;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1EventCurve v1EventCurve = (V1EventCurve) o;
    return Objects.equals(this.kind, v1EventCurve.kind) &&
        Objects.equals(this.x, v1EventCurve.x) &&
        Objects.equals(this.y, v1EventCurve.y) &&
        Objects.equals(this.annotation, v1EventCurve.annotation);
  }

  @Override
  public int hashCode() {
    return Objects.hash(kind, x, y, annotation);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1EventCurve {\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    x: ").append(toIndentedString(x)).append("\n");
    sb.append("    y: ").append(toIndentedString(y)).append("\n");
    sb.append("    annotation: ").append(toIndentedString(annotation)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

