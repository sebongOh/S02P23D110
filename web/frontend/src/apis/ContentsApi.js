import axios from "axios";
const host = "http://119.56.164.135:8000";

const ContentsApi = {
  //   requestAI: (data, callback, errorCallback) => requestAI(data, callback, errorCallback),
  imgupload: (data) => imgupload(data),
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

const imgupload = (data, callback, errorCallback) => {
  axios({
    url: `${host}/upload/`,
    method: "post",
    data: data,
    // headers: { "Content-Type": "application/json" },
  })
    .then((res) => {
      callback(res);
    })
    .catch((error) => {
      errorCallback(error);
    });
};

export default ContentsApi;
