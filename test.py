data = {
    "store": {
        "document:document": {
            "gridSize": 10,
            "name": "",
            "meta": {},
            "id": "document:document",
            "typeName": "document"
        },
        "page:page": {
            "meta": {},
            "id": "shape:KaNgWParpj5FZkGKxTA_o",
            "typeName": "shape"
        },
        "shape:KaNgWParpj5FZkGKxTA_o": {
            "x": 86.1865234375,
            "y": 91.9384765625,
            "rotation": 0,
            "isLocked": False,
            "labelColor": "black",
            "fill": "none",
            "draw": "size",
            "id": "shape:KaNgWParpj5FZkGKxTA_o",
            "typeName": "shape"
        },
        "shape:iJDxs1ZtLUcbDxb0z82AQ": {
            "color": "orange",
            "labelColor": "black",
            "fill": "none",
            "dash": "draw",
            "size": "m",
            "font": "draw",
            "text": "",
            "align": "middle",
            "vertical": "middle",
            "rotation": 0,
            "isLocked": False,
            "opacity": 1,
            "meta": {},
            "id": "shape:iJDxs1ZtLUcbDxb0z82AQ",
            "typeName": "shape"
        },
        "shape:9tKxAwTyGfQxS4fsfqJ": {
            "type": "arrow",
            "parentld": "page:page",
            "index": "a4",
            "props": {
                "data": {
                    "dash": "draw",
                    "size": "xL",
                    "fill": "none",
                    "color": "orange",
                    "labelColor": "black",
                    "bend": 0,
                    "start": {
                        "type": "point",
                        "x": 0,
                        "y": 0
                    },
                    "end": {
                        "x": 337.3193359375,
                        "y": 154.072265625,
                        "rotation": 0,
                        "isLocked": False,
                        "opacity": 1,
                        "meta": {},
                        "id": "shape:9tKxAwTyGfQxS4fsfqJ",
                        "typeName": "arrow",
                        "parentld": "page:page",
                        "index": "a4",
                        "props": {
                            "data": {
                                "dash": "draw",
                                "size": "xL",
                                "fill": "none",
                                "color": "orange",
                                "labelColor": "black"
                            }
                        },
                        "arrowheadStart": "none",
                        "arrowheadEnd": "arrow",
                        "text": "",
                        "font": "draw"
                    },
                    "arrowheadStart": "none",
                    "arrowheadEnd": "arrow",
                    "text": "",
                    "font": "draw"
                },
                "typeName": "arrow"
            },
            "schemaVersion": 1,
            "storeVersion": 4,
            "recordVersions": {
                "asset": {
                    "version": 1,
                    "subTypeKey": "type",
                    "subTypeVersions": {
                        "image": 2,
                        "video": 1
                    }
                },
                "instance_page_state": {
                    "version": 5,
                    "page": {
                        "version": 1
                    },
                    "shape": {
                        "version": 3,
                        "subTypeKey": "type"
                    }
                },
                "group": 0,
                "text": 1,
                "bookmark": 1,
                "draw": 1,
                "geo": 7,
                "note": 4,
                "line": 1,
                "frame": 0,
                "arrow": 1,
                "highlight": 0,
                "embed": 4,
                "image": 2,
                "video": 1
            },
            "version": 1
        }
    }
}

if 'store' in data:
    store_data = data['store']

    page_ids = []
    shape_ids = []

    # Iterate through the keys in store_data
    for key, value in store_data.items():
        print("key: ", key)
        if key == 'page:page':
            print("page:page: ", value['id'])
        elif 'shape:' in key:
            shape = key
            key.split(':')
            print(key[1])
