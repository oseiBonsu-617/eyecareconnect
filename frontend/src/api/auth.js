import api from "./axios";

export const getCurrentUser = async () => {
  const response = await api.get("/auth/users/me/");
  return response.data;
};
