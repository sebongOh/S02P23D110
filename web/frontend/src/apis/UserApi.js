// import axios from "axios";
// const host = "http://192.168.100.58:8080";
// const noticePort = "http://192.168.100.58:8080";
// const filehost = "http://192.168.100.58:8080";
// const UserApi = {
//   requestLogin: (data, callback, errorCallback) => requestLogin(data, callback, errorCallback),
//   join: (data) => join(data),
//   profileLoad: (data, callback, error) => profileLoad(data, callback, error),
// };
// const requestLogin = (data, callback, errorCallback) => {
//   axios
//     .post(`${host}/account/login?email=` + JSON.stringify(data["email"]) + "&password=" + JSON.stringify(data["password"]))
//     .then((res) => {
//       callback(res);
//     })
//     .catch((error) => {
//       errorCallback(error);
//     });
// };

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

// export default UserApi;
