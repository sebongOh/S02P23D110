import axios from "axios";
const host = "http://58.230.252.215:8000";

const UserApi = {
  requestLogin: (data, callback, errorCallback) => requestLogin(data, callback, errorCallback),
  requestLike: (data, callback, errorCallback) => requestLike(data, callback, errorCallback),
  //   join: (data) => join(data),
  //   profileLoad: (data, callback, error) => profileLoad(data, callback, error),
};

const requestLike = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/user/like/` + data,
    method: "post",
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

// const requestLogin = (data, callback, errorCallback) => {
//   axios({
//     url: `${host}/back/login/?identify=${data["identify"]}&password=${data["password"]}`,
//     method: "post",
//   })
//     .then((res) => {
//       console.log(res);
//       callback(res);
//     })
//     .catch((error) => {
//       console.log(error);
//       errorCallback(error);
//     });
// };

const requestLogin = (data, callback, errorCallback) => {
  axios
    .post(`${host}/back/login/`, {
      identify: data["identify"],
      password: data["password"],
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

// const join = (body) => {
//   var value = {
//     password: body.password,
//     email: body.email,

//     nickName: body.nickName,
//     name: body.name,
//     comment: body.comment,
//     keyword: body.keyword,
//     imgURL: body.imgURL,
//   };

//   axios({
//     url: `${host}/account/signup`,
//     method: "post",
//     data: JSON.stringify(value),
//     headers: { "Content-Type": "application/json" },
//   })
//     .then((res) => {
//       console.log(res);
//     })
//     .catch((error) => {
//       alert("error" + error);
//     });
// };

// const fileUpload = (data, callback, errorCallback) => {
//   // axios({
//   //     url: `${host}/account/fileUpload`,
//   //     method: 'post',
//   //     httpAgent
//   //     params: data,
//   //     success: callback,
//   //     error: errorCallback
//   // });
//   axios
//     .post(`${filehost}/account/fileUpload`, data)
//     .then(() => {
//       console.log("사진 수정 성공!!!!");
//       callback;
//     })
//     .catch(() => {
//       errorCallback;
//     });
// };

export default UserApi;
