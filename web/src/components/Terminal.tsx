
import React from 'react';
import { cn } from "@/lib/utils";

interface TerminalProps {
  children: React.ReactNode;
  className?: string;
}

const Terminal = ({ children, className }: TerminalProps) => {
  return (
    <div className={cn("bg-terminal-gray p-4 rounded-md my-4 border border-terminal-lightGray overflow-x-auto", className)}>
      <div className="flex gap-2 mb-2">
        <div className="w-3 h-3 rounded-full bg-red-500"></div>
        <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
        <div className="w-3 h-3 rounded-full bg-green-500"></div>
      </div>
      <div className="font-mono text-terminal-white text-sm">
        {children}
      </div>
    </div>
  );
};

export default Terminal;
