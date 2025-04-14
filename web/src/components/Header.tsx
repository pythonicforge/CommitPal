
import React from 'react';
import { Github } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="flex justify-between items-center py-4">
      <a 
        href="/" 
        className="font-mono text-terminal-green text-xl font-bold"
      >
        CommitPal
      </a>
      <nav>
        <a 
          href="https://github.com/pythonicforge/CommitPal" 
          target="_blank" 
          rel="noopener noreferrer"
          className="flex items-center gap-2 text-terminal-white hover:text-terminal-green transition-colors"
        >
          <Github size={18} />
          <span className="font-mono">GitHub</span>
        </a>
      </nav>
    </header>
  );
};

export default Header;
