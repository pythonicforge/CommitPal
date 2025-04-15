
import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="mt-16 py-8 border-t border-terminal-lightGray">
      <div className="container">
        <div className="flex flex-col md:flex-row justify-between items-center gap-4">
          <div className="text-center md:text-left">
            <p className="text-terminal-white opacity-80 font-mono">
              © {new Date().getFullYear()} CommitPal. Made by Hardik
            </p>
          </div>
          <div className="flex items-center gap-4">
            <a 
              href="https://github.com/pythonicforge/CommitPal" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-terminal-white opacity-80 hover:text-terminal-green transition-colors font-mono"
            >
              GitHub
            </a>
            <a 
              href="https://github.com/pythonicforge/CommitPal/blob/main/LICENSE" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-terminal-white opacity-80 hover:text-terminal-green transition-colors font-mono"
            >
              License
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
