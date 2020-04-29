import axios from "axios";
const host = "http://58.230.252.215:8080";

const ContentsApi = {
  //   requestAI: (data, callback, errorCallback) => requestAI(data, callback, errorCallback),
  imgupload: (data, callback, errorCallback) => imgupload(data, callback, errorCallback),
  search: (data, callback, errorCallback) => search(data, callback, errorCallback),
  requestCarDetail: (data, callback, errorCallback) => requestCarDetail(data, callback, errorCallback),
  requestCars: (callback, errorCallback) => requestCars(callback, errorCallback),
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
    url: `${host}/back/upload/`,
    method: "post",
    data: formdata,
    headers: {
      "Content-Type": "multipart/form-data",
    },
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
    url: `${host}/back/cars/company/` + data,
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

const requestCarDetail = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/cars/` + data,
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

const requestCars = (callback, errorCallback) => {
  axios({
    url: `${host}/back/cars`,
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
