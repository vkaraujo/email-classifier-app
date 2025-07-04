export default function UploadHistory({ lastResults, onSelectHistory }) {
  if (!lastResults.length) return null;

  return (
    <div className="mt-8">
      <h3 className="font-semibold mb-2 text-gray-500">
        Histórico (clique para visualizar):
      </h3>
      <ul className="space-y-2">
        {lastResults.map((r, i) => {
          let bg = "bg-gray-50 border-gray-300";
          if (r.categoria === "Produtivo") bg = "bg-green-50 border-green-400";
          if (r.categoria === "Improdutivo") bg = "bg-red-50 border-red-400";

          return (
            <li 
              key={i} 
              onClick={() => onSelectHistory(r)}
              className={`p-2 border rounded cursor-pointer transform transition duration-200 
                hover:scale-[1.02] hover:shadow-lg hover:border-gray-500 ${bg}`}
            >
              <strong>{r.file || "Texto inserido"}</strong>: {r.categoria}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
