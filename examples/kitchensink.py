import sys
import time

sys.path.append("../src")

from glootil import Toolbox

tb = Toolbox(
    "kitchensink",
    "Kitchen Sink Extension",
    "Examples covering as many capabilities as possible",
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


def now_ms_ts():
    return time.time() * 1000


tb.serve("127.0.0.1", 8088)
