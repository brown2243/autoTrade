const axios = require("axios");

const axiosInstance = axios.create({
  // baseURL: Config.gateWayServerUrl,
  timeout: 3000,
  headers: {
    "Content-Type": "application/json",
  },
  adapter: cacheAdapterEnhancer(axios.default.adapter, {
    enabledByDefault: false,
  }),
});

const { CancelToken } = axios;
const axiosCancelObj = {};

axiosInstance.interceptors.request.use(
  (req) => {
    const removeQueryStringUrl = req.url.split("?")[0];

    if (axiosCancelObj[removeQueryStringUrl]) {
      axiosCancelObj[removeQueryStringUrl]();

      axiosCancelObj[removeQueryStringUrl] = null;
    }
    return {
      ...req,
      removeQueryStringUrl,
      cancelToken: new CancelToken((cancelToken) => {
        axiosCancelObj[removeQueryStringUrl] = cancelToken;
      }),
    };
  },
  (err) => Promise.reject(err)
);

axiosInstance.interceptors.response.use(
  (res) => {
    const {
      config: { removeQueryStringUrl },
      //   status,
      //   data: { success, result, error },
    } = res;

    axiosCancelObj[removeQueryStringUrl] = null;

    return res;
  },
  (err) => Promise.reject(err)
);

export const cmGetAxios = (req) =>
  axiosInstance({
    ...req,
    method: "GET",
  });

export const cmPostAxios = (req) =>
  axiosInstance({
    ...req,
    method: "POST",
  });

export const cmPutAxios = (req) =>
  axiosInstance({
    ...req,
    method: "PUT",
  });

export const cmDeleteAxios = (req) =>
  axiosInstance({
    ...req,
    method: "DELETE",
  });

const cmAuthAxios = (req) => {
  const token = getAccToken();

  if (token) {
    return axiosInstance({
      ...req,
      headers: {
        ...req.headers,
        Authorization: `Bearer ${token}`,
      },
    });
  }
};

export const cmAuthGetAxios = (req) =>
  cmAuthAxios({
    ...req,
    method: "GET",
  });

export const cmAuthPostAxios = (req) =>
  cmAuthAxios({
    ...req,
    method: "POST",
  });

export const cmAuthPutAxios = (req) =>
  cmAuthAxios({
    ...req,
    method: "PUT",
  });

export const cmAuthDeleteAxios = (req) =>
  cmAuthAxios({
    ...req,
    method: "DELETE",
  });
