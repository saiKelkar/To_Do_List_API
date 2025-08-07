import React, { useState } from "react";

interface Props {
    onAdd: (text: string) => void;
}

export default function TodoInput({ onAdd }: Props) {
    const [text, setText] = useState("");

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (text.trim() !== "") {
            onAdd(text);
            setText("");
        }
    };

    return (
        <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
            <input
                type="text"
                placeholder="Add a task..."
                className="flex-1 px-4 py-2 border rounded-md"
                value={text}
                onChange={(e) => setText(e.target.value)}
            />
            <button
                type="submit"
                className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
            >
                Add
            </button>
        </form>
    );
}