
import React from 'react';

interface CommitExampleProps {
  style: string;
  message: string;
}

const CommitExample: React.FC<CommitExampleProps> = ({ style, message }) => {
  return (
    <div className="border border-terminal-lightGray rounded-md p-4 mb-4">
      <div className="flex flex-col md:flex-row md:items-center gap-2 mb-2">
        <span className="text-terminal-green font-mono font-bold">Style:</span>
        <code className="bg-terminal-gray px-2 py-0.5 rounded text-terminal-white">
          {style}
        </code>
      </div>
      <div className="bg-terminal-gray p-3 rounded">
        <p className="font-mono text-terminal-white whitespace-pre-wrap">{message}</p>
      </div>
    </div>
  );
};

export default CommitExample;
