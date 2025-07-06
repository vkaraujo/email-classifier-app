import { useState } from 'react';
import FileInput from './FileInput';
import TextInput from './TextInput';
import UploadButton from './UploadButton';
import UploadResult from './UploadResult';
import UploadHistory from './UploadHistory';
import { toast } from 'sonner';
import uploadService from '../services/uploadService';

export default function FileUploader() {
  const [files, setFiles] = useState([]);
  const [text, setText] = useState('');
  const [result, setResult] = useState([]);
  const [lastResults, setLastResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [highlight, setHighlight] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult([]);
    try {
      let currentResult = [];

      if (files.length) {
        for (const file of files) {
          const data = await uploadService.uploadFile(file);
          currentResult.push({ file: file.name, ...data });
        }
      }

      if (text.trim()) {
        const data = await uploadService.uploadText(text);
        currentResult.push({ text, ...data });
      }

      if (currentResult.length) {
        setResult(currentResult);
        setLastResults(prev => [...currentResult, ...prev].slice(0, 20));
        toast.success("Analisado com sucesso!");
        setHighlight(true);
        setTimeout(() => setHighlight(false), 1000);
      } else {
        toast.error("Selecione ao menos um arquivo ou insira texto.");
      }
    } catch (err) {
      console.error(err);
      toast.error("Falha ao processar: " + err.message);
    } finally {
      setLoading(false);
      setFiles([]);
      setText('');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white shadow-md rounded p-6 w-full max-w-4xl">
        <h1 className="text-2xl font-bold mb-4 text-center">Classificador de E-mails</h1>
        <p className="text-center text-sm text-gray-600 mb-4">
          O servidor pode levar alguns segundos para responder se estiver em repouso.
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <FileInput files={files} setFiles={setFiles} disabled={loading} />
          <TextInput text={text} setText={setText} disabled={loading} />
          <UploadButton files={files} text={text} loading={loading} />
        </form>

        <UploadResult result={result} highlight={highlight} />

        <UploadHistory 
          lastResults={lastResults}
          onSelectHistory={(item) => {
            setResult([item]);
            setHighlight(true);
            setTimeout(() => setHighlight(false), 1000);
          }}
        />
      </div>
    </div>
  );
}
