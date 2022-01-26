const create_response = (surveyData) => {
    //const data1 = {
     //   "data": [{"submission":1,"question":2,"answer":"vue2"},{"submission":1,"question":1,"answer":"1"}]
     // }

    console.log('hello world')
    postData('http://127.0.0.1:8000/api/response/', surveyData)
    .then(data => {
      console.log(data); // JSON data parsed by `data.json()` call
    });
}
// Example POST method implementation:
async function postData(url = '', data = {}) {
    // Default options are marked with *
    console.log(data)
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    console.log('hello world')
    return response.json(); // parses JSON response into native JavaScript objects
  }
  

  
export {create_response}