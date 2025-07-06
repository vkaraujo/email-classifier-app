const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";

const uploadService = {
  async uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    return data.results[0];
  },

  async uploadText(text) {
    const formData = new FormData();
    formData.append("text", text);

    const response = await fetch(`${API_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    return data.results[0];
  },
};

export default uploadService;
