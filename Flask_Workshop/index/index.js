const BACKEND_URL = "http://127.0.0.1:5000/";

const test = async () => {
    const response = await fetch(BACKEND_URL, {
        method: "GET"
    })

    const text = await response.text();
    alert(text);
}

test()


