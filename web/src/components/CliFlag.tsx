
import React from 'react';

interface CliFlagProps {
  flag: string;
  description: string;
  defaultValue?: string;
}

const CliFlag: React.FC<CliFlagProps> = ({ flag, description, defaultValue }) => {
  return (
    <div className="my-2 pb-2">
      <div className="flex flex-col md:flex-row md:items-start gap-2">
        <code className="font-mono text-terminal-green whitespace-nowrap px-2 py-0.5 bg-terminal-gray rounded">
          {flag}
        </code>
        <p className="text-terminal-white opacity-90">{description}</p>
      </div>
      {defaultValue && (
        <p className="text-sm opacity-70 mt-1 pl-3 border-l-2 border-terminal-lightGray">
          Default: <code className="text-terminal-white">{defaultValue}</code>
        </p>
      )}
    </div>
  );
};

export default CliFlag;
