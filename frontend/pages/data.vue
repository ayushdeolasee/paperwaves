<template>
    <div>
        <!-- Display JSON data -->
        <pre>{{ jsonData }}</pre>
    </div>
</template>

<script>
export default {
    data() {
        return {
            jsonData: null,
        };
    },
    mounted() {
        this.convertXMLtoJSON();
    },
    methods: {
        convertXMLtoJSON() {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = () => {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var xmlData = xhr.responseXML;
                    var jsonData = this.xmlToJson(xmlData);
                    this.jsonData = JSON.stringify(jsonData, null, 2);
                }
            };
            xhr.open(
                "GET",
                "http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1",
                true
            );
            xhr.send();
        },
        xmlToJson(xml) {
            var obj = {};
            if (xml.nodeType === 1) {
                if (xml.attributes.length > 0) {
                    obj["@attributes"] = {};
                    for (var j = 0; j < xml.attributes.length; j++) {
                        var attribute = xml.attributes.item(j);
                        obj["@attributes"][attribute.nodeName] =
                            attribute.nodeValue;
                    }
                }
            } else if (xml.nodeType === 3) {
                obj = xml.nodeValue;
            }
            if (xml.hasChildNodes()) {
                for (var i = 0; i < xml.childNodes.length; i++) {
                    var item = xml.childNodes.item(i);
                    var nodeName = item.nodeName;
                    if (typeof obj[nodeName] === "undefined") {
                        obj[nodeName] = this.xmlToJson(item);
                    } else {
                        if (typeof obj[nodeName].push === "undefined") {
                            var old = obj[nodeName];
                            obj[nodeName] = [];
                            obj[nodeName].push(old);
                        }
                        obj[nodeName].push(this.xmlToJson(item));
                    }
                }
            }
            // delete obj["#text"];
            // delete obj["@attributes"];
            // delete obj["link"];
            // delete obj["opensearch:itemsPerPage"];
            // delete obj["opensearch:startIndex"];
            // delete obj["opensearch:totalResults"];
            // delete obj["title"];
            // delete obj["updated"];
            const feed = obj["feed"];
            // console.log(feed);
            return obj;
        },
    },
};
</script>
