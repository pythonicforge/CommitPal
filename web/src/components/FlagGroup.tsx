
import React from 'react';
import CliFlag from './CliFlag';

interface Flag {
  flag: string;
  description: string;
  defaultValue?: string;
}

interface FlagGroupProps {
  title: string;
  flags: Flag[];
}

const FlagGroup: React.FC<FlagGroupProps> = ({ title, flags }) => {
  return (
    <div className="mb-8">
      <h3 className="font-mono text-xl text-terminal-green mb-3">{title}</h3>
      <div className="space-y-2">
        {flags.map((flag, index) => (
          <CliFlag 
            key={index}
            flag={flag.flag}
            description={flag.description}
          />
        ))}
      </div>
    </div>
  );
};

export default FlagGroup;
