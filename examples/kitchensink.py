import asyncio
import base64
import hashlib
import random
import sys
import time

from datetime import date
from enum import Enum

from fastapi import Request

sys.path.append("../src")
from glootil import DynEnum, ResourceInfo, Toolbox, serve_static_file


class State:
    pass


tb = Toolbox(
    "kitchensink",
    "Kitchen Sink Extension",
    "Examples covering as many capabilities as possible",
    state=State(),
)


@tb.tool
def sample_raw_markdown():
    return "# Hello\n *this* **is** markdown\n\n- one\n- two"


DIAGRAM = """sequenceDiagram
    actor User
    box Gloodata
        participant Gloodata as 🟣 Gloodata
        participant LLM as 🤖 LLM
    end

    box Extension
        participant Extension as ⚙️ Extension(s)
        participant DataSource as ☁️ Data Source(s)
    end

    Note over DataSource: APIs / Services / Files<br>Databases / Data Lake
    User->>+Gloodata: Natural Language Query
    Gloodata->>+Gloodata: List Extensions' Components
    Gloodata->>+LLM: Components + Query
    LLM->>-Gloodata: Configured Component(s)
    loop For Each Component
        Gloodata->>+Extension: Instantiate Component
        Extension->>+DataSource: Load Data
        DataSource->>-Extension: Data
        Extension->>-Gloodata: Component Information
        Gloodata->>+User: Component UI
    end
"""


@tb.tool
def sample_mermaid_diagram():
    return {"type": "Mermaid", "text": DIAGRAM}


@tb.tool
def sample_infobox():
    return {
        "type": "InfoBox",
        "columns": [
            "Number",
            ["string", "String"],
            {"id": "bool", "label": "Bool"},
            "Null Value",
            "Date",
            "Date Time",
            "Link",
            "Phone",
            "Mail",
        ],
        "row": [
            42,
            "hello",
            True,
            None,
            ["date", {"ts": now_ms_ts()}],
            ["datetime", {"ts": now_ms_ts()}],
            ["link", {"url": "https://gloodata.com", "label": "Gloodata"}],
            ["phone", {"v": "555 1234 5678"}],
            ["mail", {"v": "alice@example.com"}],
        ],
    }


@tb.tool
def sample_table():
    return {
        "type": "Table",
        "columns": [
            "Number",
            ["string", "String"],
            {"id": "bool", "label": "Bool"},
            "Null Value",
            "Date",
            "Date Time",
            "Link",
            "Phone",
            "Mail",
        ],
        "rows": [
            [
                42,
                "hello",
                True,
                None,
                ["date", {"ts": now_ms_ts()}],
                ["datetime", {"ts": now_ms_ts()}],
                ["link", {"url": "https://gloodata.com", "label": "Gloodata"}],
                ["phone", {"v": "555 1234 5678"}],
                ["mail", {"v": "alice@example.com"}],
            ],
            [
                43,
                "bye",
                False,
                None,
                ["date", {"ts": now_ms_ts()}],
                ["datetime", {"ts": now_ms_ts()}],
                [
                    "link",
                    {
                        "url": "https://gloodata.com/download",
                        "label": "Download Gloodata",
                    },
                ],
                ["phone", {"v": "555 5678 1234 "}],
                ["mail", {"v": "bob@example.com"}],
            ],
        ],
    }


@tb.tool
def sample_google_map():
    return {
        "type": "GoogleMap",
        "center": [41, 29],
        "zoom": 12,
        # https://developers.google.com/maps/documentation/javascript/reference/advanced-markers#PinElementOptions
        "pins": {
            "a": {
                "background": "#3366ff",
                "borderColor": "#6699ff",
                "glyphColor": "#0033dd",
                "scale": 1.5,
            },
            "b": {
                "background": "#ff3366",
                "borderColor": "#ff6699",
                "glyphColor": "#dd0033",
                "scale": 1,
            },
            "c": {
                "background": "#66ff33",
                "borderColor": "#99ff66",
                "glyphColor": "#33dd00",
                "scale": 1.2,
            },
        },
        "legends": {
            "myGroup1": {"label": "Group 1", "color": "#3366ff"},
            "myGroup2": {"label": "Group 2", "color": "#ff3366"},
            "myGroup3": {"label": "Group 3", "color": "#33ff66"},
        },
        "markers": [
            {
                "isCluster": True,
                "key": "myGroup1",
                "markers": [
                    {
                        "lat": 41.05,
                        "lng": 29.05,
                        "title": "Center",
                    },
                    {
                        "lat": 41.0,
                        "lng": 29.0,
                        "title": "A",
                        "pin": "a",
                    },
                    {
                        "lat": 41.1,
                        "lng": 29.0,
                        "title": "B",
                        "pin": "b",
                    },
                    {
                        "lat": 41.1,
                        "lng": 29.1,
                        "title": "C",
                        "pin": "c",
                    },
                    {
                        "lat": 41.0,
                        "lng": 29.1,
                        "title": "D",
                        "pin": {
                            "background": "#ff6633",
                            "borderColor": "#ff9966",
                            "glyphColor": "#dd3300",
                            "scale": 0.8,
                        },
                    },
                ],
            },
            {
                "isCluster": False,
                "key": "myGroup2",
                "markers": [
                    {
                        "lat": 42.05,
                        "lng": 28.05,
                        "title": "Center",
                    },
                    {
                        "lat": 42.0,
                        "lng": 28.0,
                        "title": "A",
                        "pin": "a",
                    },
                    {
                        "lat": 42.1,
                        "lng": 28.0,
                        "title": "B",
                        "pin": "b",
                    },
                    {
                        "lat": 42.1,
                        "lng": 28.1,
                        "title": "C",
                        "pin": "c",
                    },
                    {
                        "lat": 42.0,
                        "lng": 28.1,
                        "title": "D",
                        "pin": {
                            "background": "#ff6633",
                            "borderColor": "#ff9966",
                            "glyphColor": "#dd3300",
                            "scale": 0.8,
                        },
                    },
                ],
            },
        ],
        # https://developers.google.com/maps/documentation/javascript/reference/polygon#PolylineOptions
        "polylines": [
            {
                "key": "myGroup2",
                "strokeColor": "#ff5522",
                "strokeOpacity": 0.5,
                "strokeWeight": 10,
                "path": [
                    {"lat": 41.0, "lng": 29.0},
                    {"lat": 41.1, "lng": 29.0},
                    {"lat": 41.1, "lng": 29.1},
                    {"lat": 41.0, "lng": 29.1},
                    {"lat": 41.0, "lng": 29.0},
                ],
            },
        ],
        "polygons": [
            {
                "key": "myGroup3",
                "strokeColor": "#22ff55",
                "strokeOpacity": 0.7,
                "strokeWeight": 5,
                "fillColor": "#22ff55",
                "fillOpacity": 0.4,
                "path": [
                    {"lat": 41.02, "lng": 29.02},
                    {"lat": 41.08, "lng": 29.02},
                    {"lat": 41.08, "lng": 29.08},
                    {"lat": 41.02, "lng": 29.08},
                    {"lat": 41.02, "lng": 29.02},
                ],
            },
        ],
        "heatmaps": [
            {
                "key": "myGroup3",
                # https://developers.google.com/maps/documentation/javascript/reference/visualization#HeatmapLayerOptions
                "points": [
                    [42.02, 31.02],
                    [42.04, 31.04, 2],
                    [42.06, 31.06, 3],
                    [42.08, 31.08, 4],
                    [42.1, 31.1, 5],
                ],
            },
        ],
    }


@tb.tool
def sample_population_pyramid():
    return {
        "type": "PopulationPyramid",
        "items": [
            {"label": "90-100", "start": 10, "end": 12, "startLabel": "ten!"},
            {"label": "80-90", "start": 230, "end": 251, "endLabel": "hi!"},
            {"label": "70-80", "start": 330, "end": 361, "endSize": 50},
            {"label": "60-70", "start": 430, "end": 471, "startSize": 50},
            {"label": "50-60", "start": 530, "end": 551},
            {"label": "40-50", "start": 630, "end": 661},
            {"label": "30-40", "start": 730, "end": 781},
            {"label": "20-30", "start": 830, "end": 851},
            {"label": "10-20", "start": 930, "end": 991},
            {"label": "0-10", "start": 1030, "end": 1021},
        ],
    }


@tb.tool
def sample_area_map():
    return {
        "type": "AreaMap",
        "mapId": "world",
        "colorMap": "jet",
        "items": [
            {"name": "AR", "value": 1},
            {"name": "BR", "value": None},
            {"name": "FR", "value": 2, "color": "orange"},
            {"name": "IT", "value": 3},
            {"name": "CA", "value": 5},
            {"name": "MX", "value": 6},
            {"name": "JP", "value": 7},
            {"name": "CN", "value": 8},
            {"name": "AU", "value": 9},
            {"name": "NZ", "value": 10},
        ],
    }


@tb.task
async def search_handler(query: str = ""):
    await asyncio.sleep(random.uniform(1, 5))

    return [
        {"type": "Post", "body": f"Query: '{query}'"},
        {
            "type": "Post",
            "format": "txt",
            "title": "Plain text",
            "body": "plain *text* **really**",
        },
        {
            "type": "Post",
            "format": "md",
            "title": "Markdown",
            "body": "some *markdown* **formatting**.",
        },
    ]


SEARCH_HANDLER_ID = tb.handler_id_for_task(search_handler)


@tb.tool
def sample_search():
    return {
        "type": "Search",
        "placeholder": "Search...",
        "searchType": "submit",
        "searchHandlerName": SEARCH_HANDLER_ID,
    }


SAMPLE_DOCUMENT_RESOURCE_TYPE = "sample-doc"


@tb.tool
def show_sample_document():
    return {
        "type": "Pdf",
        "resource": {"type": SAMPLE_DOCUMENT_RESOURCE_TYPE, "id": "book", "page": 5},
    }


@tb.resource(for_type=SAMPLE_DOCUMENT_RESOURCE_TYPE)
def pdf_resource(request: Request, resource: ResourceInfo):
    if resource.id == "book":
        return serve_static_file("./book.pdf", request)


@tb.resource(for_type="code")
def code_resource(state: State, request: Request, resource: ResourceInfo):
    if resource.id == "kitchensink":
        return serve_static_file("./kitchensink.py", request)
    else:
        return None


@tb.enum
class Op(Enum):
    "the operation to apply"

    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"


@tb.tool
def calculate(a: float = 0, op: Op = Op.ADD, b: float = 0):
    r = 0
    match op:
        case Op.ADD:
            r = a + b
        case Op.SUB:
            r = a - b
        case Op.MUL:
            r = a * b
        case Op.DIV:
            r = a / b
        case _:
            r = 0

    return f"`{op}({a}, {b}) = {r}`"


@tb.context_action(tool=calculate, target=Op)
def calculate_context_action():
    return [
        {"args": {"a": 5, "op": Op.ADD, "b": 10}},
        {"args": {"a": 5, "op": Op.SUB, "b": 10}},
        {"args": {"a": 5, "op": Op.MUL, "b": 10}},
        {"args": {"a": 5, "op": Op.DIV, "b": 10}},
    ]


@tb.enum
class Country(DynEnum):
    @staticmethod
    def load():
        return [
            ("US", "United States"),
            ("CA", "Canada"),
            ("MX", "Mexico"),
            ("FR", "France"),
            ("DE", "Germany"),
            ("IT", "Italy"),
            ("CN", "China"),
            ("JP", "Japan"),
            ("IN", "India"),
            ("BR", "Brazil"),
            ("AR", "Argentina"),
            ("CO", "Colombia"),
            ("ZA", "South Africa"),
            ("NG", "Nigeria"),
            ("EG", "Egypt"),
            ("AU", "Australia"),
            ("NZ", "New Zealand"),
            ("FJ", "Fiji"),
        ]


DEFAULT_COUNTRY = Country("FJ", "Fiji")


@tb.tool
def country_information(country: Country = DEFAULT_COUNTRY):
    return f"# Country Info\n\nCode: `{country.name}`\n\nName: {country.value}"


@tb.tool
def show_date(d: date):
    d = d if d else date.today()
    return f"Date: {d}"


@tb.enum
class DateDiffUnit(Enum):
    DAYS = "Days"
    WEEKS = "Weeks"
    MONTHS = "Months"
    YEARS = "Years"


@tb.tool(
    name="Date Difference",
    args={
        "a": {
            "name": "From",
            "docs": "The starting date, default to one week ago from today if not provided",
        },
        "b": {"name": "To", "docs": "The end date, default to today if not provided"},
        "unit": {"name": "Unit", "docs": "The unit of time to use for the difference"},
    },
    examples=[
        "days between the moon landing and first barack obama inauguration",
        "years between the first flight and the moon landing",
    ],
)
def date_diff(a: date, b: date, unit: DateDiffUnit = DateDiffUnit.DAYS):
    b = b if b else date.today()
    a = a if a else b or date.today()

    in_days = (b - a).days

    if unit == DateDiffUnit.WEEKS:
        d = in_days / 7
    elif unit == DateDiffUnit.MONTHS:
        d = in_days / 30
    elif unit == DateDiffUnit.YEARS:
        d = in_days / 365
    else:
        d = in_days

    d = int(d)
    return f"Difference between {a} and {b}: {d} {unit.value}"


def now_ms_ts():
    return time.time() * 1000


@tb.enum(icon="thermometer")
class TemperatureTransform(Enum):
    """the temperature transformation to apply"""

    CELSIUS_TO_FAHRENHEIT = "Celsius to Fahrenheit"
    FAHRENHEIT_TO_CELSIUS = "Fahrenheit to Celsius"


@tb.tool(
    name="Temperature Converter",
    examples=["Convert 100 Celsius to Fahrenheit", "Convert 212 Fahrenheit to Celsius"],
    args={
        "temperature": {"name": "Temperature", "docs": "The temperature to convert"},
        "transform": {"name": "Transform"},
    },
)
def temperature_converter(
    temperature: float = 36.0,
    transform: TemperatureTransform = TemperatureTransform.CELSIUS_TO_FAHRENHEIT,
):
    if transform == TemperatureTransform.CELSIUS_TO_FAHRENHEIT:
        result = round((temperature * 9 / 5) + 32, 2)
        return f"{temperature}°C is equal to {result}°F"
    elif transform == TemperatureTransform.FAHRENHEIT_TO_CELSIUS:
        result = round((temperature - 32) * 5 / 9, 2)
        return f"{temperature}°F is equal to {result}°C"
    else:
        return "Invalid transformation type"


@tb.enum(icon="unit")
class MetricDistanceUnits(Enum):
    """the metric distance unit to use"""

    KILOMETERS = "Kilometers"
    METERS = "Meters"
    CENTIMETERS = "Centimeters"
    MILLIMETERS = "Millimeters"


@tb.enum(icon="unit")
class ImperialDistanceUnits(Enum):
    """the imperial distance unit to use"""

    MILES = "Miles"
    YARDS = "Yards"
    FEET = "Feet"
    INCHES = "Inches"


@tb.tool(
    name="Metric to Imperial Distance Converter",
    examples=["Convert 100 kilometers to miles", "Convert 50 centimeters to inches"],
    args={
        "distance": {"name": "Distance", "docs": "The distance to convert"},
        "from_unit": {"name": "From Unit"},
        "to_unit": {"name": "To Unit"},
    },
)
def metric_to_imperial_distance_converter(
    distance: float = 1.0,
    from_unit: MetricDistanceUnits = MetricDistanceUnits.KILOMETERS,
    to_unit: ImperialDistanceUnits = ImperialDistanceUnits.MILES,
):
    distance_in_mm = distance
    if from_unit == MetricDistanceUnits.KILOMETERS:
        distance_in_mm *= 1_000_000
    elif from_unit == MetricDistanceUnits.METERS:
        distance_in_mm *= 1_000
    elif from_unit == MetricDistanceUnits.CENTIMETERS:
        distance_in_mm *= 10
    elif from_unit == MetricDistanceUnits.MILLIMETERS:
        pass

    result = distance_in_mm
    # TODO: check this numbers :)
    if to_unit == ImperialDistanceUnits.MILES:
        result /= 1_609_344
    elif to_unit == ImperialDistanceUnits.YARDS:
        result /= 914.4
    elif to_unit == ImperialDistanceUnits.FEET:
        result /= 304.8
    elif to_unit == ImperialDistanceUnits.INCHES:
        result /= 25.4

    result = round(result, 2)

    return f"{distance} {from_unit.value} is equal to {result} {to_unit.value}"


@tb.enum(icon="calculator")
class EncodeAlgorithm(Enum):
    """the encoding algorithm to use"""

    SHA256 = "SHA256"
    SHA512 = "SHA512"
    MD5 = "MD5"
    BASE64 = "Base64"


@tb.tool(
    name="Hash Text",
    args={"text": {"name": "Text", "multiline": True}, "algorithm": "Algorithm"},
)
def encode_text(
    text: str = "Hello World", algorithm: EncodeAlgorithm = EncodeAlgorithm.SHA256
):
    if algorithm == EncodeAlgorithm.SHA256:
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        return f"SHA256 Hash: `{sha256_hash}`"
    if algorithm == EncodeAlgorithm.SHA512:
        sha512_hash = hashlib.sha512(text.encode()).hexdigest()
        return f"SHA512 Hash: `{sha512_hash}`"
    elif algorithm == EncodeAlgorithm.MD5:
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        return f"MD5 Hash: `{md5_hash}`"
    elif algorithm == EncodeAlgorithm.BASE64:
        base64_result = base64.b64encode(text.encode()).decode()
        return f"Base64 Encoding: `{base64_result}`"
    else:
        return "Invalid algorithm"


tb.serve_from_env_or(default_port=8088)
