#!/usr/bin/python
#
# Copyright 2018-2023 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime
import json

from collections import namedtuple
from typing import Dict, List, Mapping, Optional, Union

from clipped.config.parser import ConfigParser
from clipped.config.schema import skip_partial
from clipped.utils.csv import validate_csv
from clipped.utils.dates import parse_datetime
from clipped.utils.enums import PEnum
from clipped.utils.np import sanitize_np_types
from clipped.utils.tz import now
from pydantic import StrictStr, root_validator

from polyaxon.schemas.base import BaseSchemaModel
from traceml.artifacts.kinds import V1ArtifactKind


class SearchView(str, PEnum):
    ANY = "any"
    RUNS = "runs"
    SELECTION = "selection"
    ANALYTICS = "analytics"
    COMPONENTS = "components"
    MODELS = "models"
    ARTIFACTS = "artifacts"
    PROJECTS = "projects"


class V1EventImage(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.IMAGE

    height: Optional[int]
    width: Optional[int]
    colorspace: Optional[int]
    path: Optional[StrictStr]


class V1EventVideo(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.VIDEO

    height: Optional[int]
    width: Optional[int]
    colorspace: Optional[int]
    path: Optional[StrictStr]
    content_type: Optional[StrictStr]


class V1EventDataframe(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.DATAFRAME

    path: Optional[StrictStr]
    content_type: Optional[StrictStr]


class V1EventHistogram(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.HISTOGRAM

    values: Optional[List[float]]
    counts: Optional[List[float]]


class V1EventAudio(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.AUDIO

    sample_rate: Optional[float]
    num_channels: Optional[int]
    length_frames: Optional[int]
    path: Optional[StrictStr]
    content_type: Optional[StrictStr]


class V1EventChartKind(str, PEnum):
    PLOTLY = "plotly"
    BOKEH = "bokeh"
    VEGA = "vega"


class V1EventChart(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.CHART

    kind: Optional[V1EventChartKind]
    figure: Optional[Dict]

    def to_json(self, humanize_values=False, include_kind=False, include_version=False):
        if self.kind == V1EventChartKind.PLOTLY:
            import plotly.tools

            obj = self.to_dict(
                humanize_values=humanize_values,
                include_kind=include_kind,
                include_version=include_version,
            )
            return json.dumps(obj, cls=plotly.utils.PlotlyJSONEncoder)
        # Resume normal serialization
        return super().to_json(
            humanize_values=humanize_values,
            include_kind=include_kind,
            include_version=include_version,
        )


class V1EventCurveKind(str, PEnum):
    ROC = "roc"
    PR = "pr"
    CUSTOM = "custom"


class V1EventCurve(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.CURVE

    kind: Optional[V1EventCurveKind]
    x: Optional[List[float]]
    y: Optional[List[float]]
    annotation: Optional[StrictStr]


class V1EventConfusionMatrix(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.CONFUSION

    x: Optional[List]
    y: Optional[List]
    z: Optional[List]


class V1EventArtifact(BaseSchemaModel):
    _IDENTIFIER = "artifact"

    kind: Optional[V1ArtifactKind]
    path: Optional[StrictStr]


class V1EventModel(BaseSchemaModel):
    _IDENTIFIER = V1ArtifactKind.MODEL

    framework: Optional[StrictStr]
    path: Optional[StrictStr]
    spec: Optional[Dict]


class V1Event(BaseSchemaModel):
    _SEPARATOR = "|"
    _IDENTIFIER = "event"

    timestamp: Optional[datetime.datetime]
    step: Optional[int]
    metric: Optional[float]
    image: Optional[V1EventImage]
    histogram: Optional[V1EventHistogram]
    audio: Optional[V1EventAudio]
    video: Optional[V1EventVideo]
    html: Optional[str]
    text: Optional[str]
    chart: Optional[V1EventChart]
    curve: Optional[V1EventCurve]
    confusion: Optional[V1EventConfusionMatrix]
    artifact: Optional[V1EventArtifact]
    model: Optional[V1EventModel]
    dataframe: Optional[V1EventDataframe]

    @root_validator(pre=True)
    @skip_partial
    def pre_validate(cls, values):
        v = values.get(V1ArtifactKind.IMAGE)
        get_dict = ConfigParser.parse(Dict)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.IMAGE] = get_dict(
                key=V1ArtifactKind.IMAGE,
                value=v,
            )
        v = values.get(V1ArtifactKind.HISTOGRAM)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.HISTOGRAM] = get_dict(
                key=V1ArtifactKind.HISTOGRAM,
                value=v,
            )
        v = values.get(V1ArtifactKind.AUDIO)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.AUDIO] = get_dict(
                key=V1ArtifactKind.AUDIO,
                value=v,
            )
        v = values.get(V1ArtifactKind.VIDEO)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.VIDEO] = get_dict(
                key=V1ArtifactKind.VIDEO,
                value=v,
            )
        v = values.get(V1ArtifactKind.CHART)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.CHART] = get_dict(
                key=V1ArtifactKind.CHART,
                value=v,
            )
        v = values.get(V1ArtifactKind.CURVE)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.CURVE] = get_dict(
                key=V1ArtifactKind.CURVE,
                value=v,
            )
        v = values.get(V1ArtifactKind.CONFUSION)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.CONFUSION] = get_dict(
                key=V1ArtifactKind.CONFUSION,
                value=v,
            )
        v = values.get(V1ArtifactKind.ARTIFACT)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.ARTIFACT] = get_dict(
                key=V1ArtifactKind.ARTIFACT,
                value=v,
            )
        v = values.get(V1ArtifactKind.MODEL)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.MODEL] = get_dict(
                key=V1ArtifactKind.MODEL,
                value=v,
            )
        v = values.get(V1ArtifactKind.DATAFRAME)
        if v is not None and not isinstance(v, BaseSchemaModel):
            values[V1ArtifactKind.DATAFRAME] = get_dict(
                key=V1ArtifactKind.DATAFRAME,
                value=v,
            )

        return values

    @root_validator
    @skip_partial
    def validate_event(cls, values):
        count = 0

        def increment(c):
            c += 1
            if c > 1:
                raise ValueError(
                    "An event should have one and only one primitive, found {}.".format(
                        c
                    )
                )
            return c

        if values.get(V1ArtifactKind.METRIC) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.IMAGE) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.HISTOGRAM) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.AUDIO) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.VIDEO) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.HTML) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.TEXT) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.CHART) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.CURVE) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.CONFUSION) is not None:
            count = increment(count)
        if values.get("artifact") is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.MODEL) is not None:
            count = increment(count)
        if values.get(V1ArtifactKind.DATAFRAME) is not None:
            count = increment(count)

        if count != 1:
            raise ValueError(
                "An event should have one and only one primitive, found {}.".format(
                    count
                )
            )

        return values

    @classmethod
    def make(
        cls,
        step: Optional[int] = None,
        timestamp=None,
        metric: float = None,
        image: V1EventImage = None,
        histogram: V1EventHistogram = None,
        audio: V1EventAudio = None,
        video: V1EventVideo = None,
        html: Optional[str] = None,
        text: Optional[str] = None,
        chart: V1EventChart = None,
        curve: V1EventCurve = None,
        confusion: V1EventConfusionMatrix = None,
        artifact: V1EventArtifact = None,
        model: V1EventModel = None,
        dataframe: V1EventDataframe = None,
    ) -> "V1Event":
        if isinstance(timestamp, str):
            try:
                timestamp = parse_datetime(timestamp)
            except Exception as e:
                raise ValueError("Received an invalid timestamp") from e

        return cls(
            timestamp=timestamp if timestamp else now(tzinfo=True),
            step=step,
            metric=metric,
            image=image,
            histogram=histogram,
            audio=audio,
            video=video,
            html=html,
            text=text,
            chart=chart,
            curve=curve,
            confusion=confusion,
            artifact=artifact,
            model=model,
            dataframe=dataframe,
        )

    def get_value(self, dump=True):
        if self.metric is not None:
            return str(self.metric) if dump else self.metric
        if self.image is not None:
            return self.image.to_json() if dump else self.image
        if self.histogram is not None:
            return self.histogram.to_json() if dump else self.histogram
        if self.audio is not None:
            return self.audio.to_json() if dump else self.audio
        if self.video is not None:
            return self.video.to_json() if dump else self.video
        if self.html is not None:
            return self.html
        if self.text is not None:
            return self.text
        if self.chart is not None:
            return self.chart.to_json() if dump else self.chart
        if self.curve is not None:
            return self.curve.to_json() if dump else self.curve
        if self.confusion is not None:
            return self.confusion.to_json() if dump else self.confusion
        if self.artifact is not None:
            return self.artifact.to_json() if dump else self.artifact
        if self.model is not None:
            return self.model.to_json() if dump else self.model
        if self.dataframe is not None:
            return self.dataframe.to_json() if dump else self.dataframe

    def to_csv(self) -> str:
        values = [
            str(self.step) if self.step is not None else "",
            str(self.timestamp) if self.timestamp is not None else "",
            self.get_value(dump=True),
        ]

        return self._SEPARATOR.join(values)


class V1Events:
    ORIENT_CSV = "csv"
    ORIENT_DICT = "dict"

    def __init__(self, kind, name, df):
        self.kind = kind
        self.name = name
        self.df = df

    @classmethod
    def read(
        cls, kind: str, name: str, data: Union[str, Dict], parse_dates: bool = True
    ) -> "V1Events":
        import pandas as pd

        if isinstance(data, str):
            csv = validate_csv(data)
            if parse_dates:
                df = pd.read_csv(
                    csv,
                    sep=V1Event._SEPARATOR,
                    parse_dates=["timestamp"],
                )
            else:
                df = pd.read_csv(
                    csv,
                    sep=V1Event._SEPARATOR,
                )
        elif isinstance(data, dict):
            df = pd.DataFrame.from_dict(data)
        else:
            raise ValueError(
                "V1Events received an unsupported value type: {}".format(type(data))
            )

        return cls(name=name, kind=kind, df=df)

    def to_dict(self, orient: str = "list") -> Dict:
        import numpy as np

        return self.df.replace({np.nan: None}).to_dict(orient=orient)

    def get_event_at(self, index):
        event = self.df.iloc[index].to_dict()
        event["timestamp"] = event["timestamp"].isoformat()
        event["step"] = sanitize_np_types(event["step"])
        return V1Event.from_dict(event)

    def _get_step_summary(self) -> Optional[Dict]:
        _count = self.df.step.count()
        if _count == 0:
            return None

        return {
            "count": sanitize_np_types(_count),
            "min": sanitize_np_types(self.df.step.iloc[0]),
            "max": sanitize_np_types(self.df.step.iloc[-1]),
        }

    def _get_ts_summary(self) -> Optional[Dict]:
        _count = self.df.timestamp.count()
        if _count == 0:
            return None

        return {
            "min": self.df.timestamp.iloc[0].isoformat(),
            "max": self.df.timestamp.iloc[-1].isoformat(),
        }

    def get_summary(self) -> Dict:
        summary = {"is_event": True}
        step_summary = self._get_step_summary()
        if step_summary:
            summary["step"] = step_summary

        ts_summary = self._get_ts_summary()
        if ts_summary:
            summary["timestamp"] = ts_summary

        if self.kind == V1ArtifactKind.METRIC:
            summary[self.kind] = {
                k: sanitize_np_types(v)
                for k, v in self.df.metric.describe().to_dict().items()
            }
            summary[self.kind]["last"] = sanitize_np_types(self.df.metric.iloc[-1])

        return summary


class LoggedEventSpec(namedtuple("LoggedEventSpec", "name kind event")):
    pass


class LoggedEventListSpec(namedtuple("LoggedEventListSpec", "name kind events")):
    def get_csv_header(self) -> str:
        return V1Event._SEPARATOR.join(["step", "timestamp", self.kind])

    def get_csv_events(self) -> str:
        events = ["\n{}".format(e.to_csv()) for e in self.events]
        return "".join(events)

    def empty_events(self):
        self.events[:] = []

    def to_dict(self):
        return {
            "name": self.name,
            "kind": self.kind,
            "events": [e.to_dict() for e in self.events],
        }

    @classmethod
    def from_dict(cls, value: Mapping) -> "LoggedEventListSpec":
        return cls(
            name=value.get("name"),
            kind=value.get("kind"),
            events=[V1Event.from_dict(e) for e in value.get("events", [])],
        )
