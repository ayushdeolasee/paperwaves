// API URL
const apiUrl =
    "http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1";

// Fetch data from the API
fetch(apiUrl)
    .then((response) => response.text())
    .then((data) => {
        // Process the XML data or perform any desired operations
        console.log(data);
    })
    .catch((error) => {
        console.error("Error occurred:", error);
    });

// Example XML data
const xmlData = `
<root>
    <item>
        <title>Item 1</title>
        <description>Description of Item 1</description>
    </item>
    <item>
        <title>Item 2</title>
        <description>Description of Item 2</description>
    </item>
</root>
`;

// Create a DOMParser instance
const parser = new DOMParser();

// Parse the XML data
const xmlDoc = parser.parseFromString(xmlData, "text/xml");

// Access elements in the XML document
const items = xmlDoc.getElementsByTagName("item");

// Process each item
for (let i = 0; i < items.length; i++) {
    const item = items[i];
    const title = item.getElementsByTagName("title")[0].textContent;
    const description = item.getElementsByTagName("description")[0].textContent;

    console.log("Title:", title);
    console.log("Description:", description);
}
