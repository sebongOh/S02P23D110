import axios from "axios";
const host = "http://119.56.164.135:8000";

const ContentsApi = {
  //   requestAI: (data, callback, errorCallback) => requestAI(data, callback, errorCallback),
  imgupload: (data, callback, errorCallback) => imgupload(data, callback, errorCallback),
  search: (data, callback, errorCallback) => search(data, callback, errorCallback),
  //   profileLoad: (data, callback, error) => profileLoad(data, callback, error),
};

// const requestAI = (data, callback, errorCallback) => {
//   axios
//     .post(`${host}/=` + JSON.stringify(data["email"]) + "&password=" + JSON.stringify(data["password"]))
//     .then((res) => {
//       callback(res);
//     })
//     .catch((error) => {
//       errorCallback(error);
//     });

const imgupload = (formdata, callback, errorCallback) => {
  axios({
    url: `${host}/upload/`,
    method: "post",
    data: formdata,
    headers: { "Content-Type": "multipart/form-data" },
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const search = (data, callback, errorCallback) => {
  axios({
    url: `${host}/search?keyword=` + data,
    method: "get",
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

export default ContentsApi;
