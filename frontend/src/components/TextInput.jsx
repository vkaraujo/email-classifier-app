export default function TextInput({ text, setText, disabled }) {
  return (
    <textarea
      value={text}
      onChange={(e) => setText(e.target.value)}
      placeholder="Ou cole o conteúdo do email aqui..."
      disabled={disabled}
      className="w-full p-3 border rounded resize-none focus:outline-none focus:ring"
      rows={6}
    />
  );
}
