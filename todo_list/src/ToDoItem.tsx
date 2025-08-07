interface Props {
  id: number;
  text: string;
  done: boolean;
  onToggle: () => void;
  onDelete: () => void;
}

export default function TodoItem({ text, done, onToggle, onDelete }: Props) {
  return (
    <div className="flex justify-between items-center p-2 border-b">
      <label className="flex items-center gap-2">
        <input type="checkbox" checked={done} onChange={onToggle} />
        <span className={done ? "line-through text-gray-400" : ""}>{text}</span>
      </label>
      <button
        onClick={onDelete}
        className="text-red-500 hover:text-red-700 text-sm"
      >
        Delete
      </button>
    </div>
  );
}