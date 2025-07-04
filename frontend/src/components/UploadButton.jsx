export default function UploadButton({ files, text, loading }) {
  const isDisabled = (!files.length && !text.trim()) || loading;

  return (
    <button 
      type="submit"
      disabled={isDisabled}
      className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 disabled:opacity-50 flex justify-center items-center"
    >
      {loading ? (
        <>
          <svg className="animate-spin h-5 w-5 mr-2 text-white" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"/>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"/>
          </svg>
          Analisando...
        </>
      ) : files.length 
          ? `Enviar ${files.length} arquivo(s)`
          : text.trim() 
            ? "Enviar texto"
            : "Selecione arquivos ou texto"}
    </button>
  );
}
