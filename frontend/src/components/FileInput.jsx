import { useRef, useEffect } from "react";

export default function FileInput({ files, setFiles, disabled }) {
  const inputRef = useRef();

  useEffect(() => {
    if (!files.length && inputRef.current) {
      inputRef.current.value = "";
    }
  }, [files]);

  const handleDrop = (e) => {
    e.preventDefault();
    setFiles([...e.dataTransfer.files]);
  };

  return (
    <div
      onDrop={handleDrop}
      onDragOver={(e) => e.preventDefault()}
      className={`border-2 border-dashed p-4 rounded text-center cursor-pointer 
        hover:bg-gray-50 ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}
    >
      <input
        type="file"
        multiple
        accept=".txt,.pdf"
        ref={inputRef}
        disabled={disabled}
        onChange={(e) => setFiles([...e.target.files])}
        className="hidden"
        id="file-upload"
      />
      <label htmlFor="file-upload" className="cursor-pointer">
        {files.length > 0
          ? `${files.length} arquivo(s) selecionado(s)`
          : "Clique ou arraste um ou mais arquivos aqui"}
      </label>
    </div>
  );
}
