export default function UploadResult({ result, highlight }) {
  if (!result.length) return null;

  return (
    <div className={`mt-6 p-4 rounded shadow-inner transition-colors duration-500 
                    ${highlight ? 'bg-blue-100' : 'bg-gray-50'}`}>
      {result.map((r, i) => (
        <div key={i} className="mb-6 border-b pb-4">
          <div className="flex justify-between items-center mb-2">
            <strong>{r.file ? `Arquivo: ${r.file}` : "Texto inserido"}</strong>
            <span className={`ml-2 px-2 py-0.5 text-xs font-semibold rounded 
              ${r.categoria === "Produtivo" ? "bg-green-200 text-green-800" :
                r.categoria === "Improdutivo" ? "bg-red-200 text-red-800" : "bg-gray-200 text-gray-800"}`}>
              {r.categoria}
            </span>
          </div>
          <p><strong>Resposta sugerida:</strong> {r.resposta_sugerida}</p>
        </div>
      ))}
    </div>
  );
}
