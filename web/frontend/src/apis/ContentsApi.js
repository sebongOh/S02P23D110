import axios from "axios";
const host = "http://58.230.252.215:8000";
<<<<<<< HEAD
// const host = "http://119.56.164.135:8000";
=======
>>>>>>> 449d0db5d99de9c7454c7595a152d0c2fee996ec

const ContentsApi = {
  //   requestAI: (data, callback, errorCallback) => requestAI(data, callback, errorCallback),
  imgupload: (data, callback, errorCallback) => imgupload(data, callback, errorCallback),
  searchCompany: (data, callback, errorCallback) => searchCompany(data, callback, errorCallback),
  searchName: (data, callback, errorCallback) => searchName(data, callback, errorCallback),
  requestCarDetail: (data, callback, errorCallback) => requestCarDetail(data, callback, errorCallback),
  requestCarAI: (data, callback, errorCallback) => requestAI(data, callback, errorCallback),
  requestCars: (callback, errorCallback) => requestCars(callback, errorCallback),
  //   profileLoad: (data, callback, error) => profileLoad(data, callback, error),
};

const requestAI = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/ai/num/${data}/`,
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

const searchCompany = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/cars/company/${data}/`,
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

const searchName = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/cars/name/${data}/`,
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
