const uploadService = {
  async uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    return data.results[0];
  },

  async uploadText(text) {
    const formData = new FormData();
    formData.append("text", text);

    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    return data.results[0];
  },
};

export default uploadService;
