import React from 'react';
import Header from '@/components/Header';
import Terminal from '@/components/Terminal';
import FlagGroup from '@/components/FlagGroup';
import CommitExample from '@/components/CommitExample';
import Footer from '@/components/Footer';
import { ArrowRight, ChevronRight, Code, Terminal as TerminalIcon, AlertCircle, BookOpen, Heart, Zap, GitBranch, Rocket } from 'lucide-react';
import { motion } from 'framer-motion';

const Index = () => {

  const aiFlags = [
    { 
      flag: "--style=<style>", 
      description: "Commit style to use (conventional, emoji, detailed, minimal, changelog)", 
      defaultValue: "conventional" 
    }
  ];

  const changelogFlags = [
    { 
      flag: "--changelog", 
      description: "Generate changelog entry" 
    },
  ];

  const gitFlags = [
    {
      flag: "--auto-push",
      description: "Automatically commits and pushes code to GitHub"
    }
  ]


  return (
    <div className="min-h-screen bg-terminal-black text-terminal-white font-sans">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        <Header />
        
        <motion.section 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center py-16 md:py-24 relative overflow-hidden"
        >
          <div className="absolute inset-0 bg-gradient-to-br from-terminal-green/10 via-terminal-green/5 to-transparent opacity-50 blur-3xl -z-10 animate-pulse"></div>
          
          <motion.div 
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.4, delay: 0.2 }}
            className="inline-flex items-center gap-2 bg-terminal-lightGray px-3 py-1 rounded-full text-sm mb-6 shadow-lg"
          >
            <span className="inline-block w-3 h-3 rounded-full bg-terminal-green animate-pulse"></span>
            <span className="font-mono opacity-90">v1.0.0</span>
          </motion.div>

          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.3 }}
            className="text-4xl md:text-5xl lg:text-6xl font-bold font-mono mb-4 text-terminal-white flex flex-col items-center justify-center"
          >
            <span>Commit</span>
            <span className="text-terminal-green">Pal</span>
          </motion.h1>

          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="text-xl md:text-2xl opacity-90 mb-8 flex items-center justify-center gap-2"
          >
            <Zap className="text-terminal-green" size={24} />
            Your AI Commit Sidekick for Smarter Git Workflows
            <GitBranch className="text-terminal-green" size={24} />
          </motion.p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-8">
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5, delay: 0.5 }}
            >
              <Terminal className="text-left inline-block">
                <span className="text-gray-400">$</span> (commitpal) diff --changelog
              </Terminal>
            </motion.div>
          </div>

          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.6 }}
            className="flex justify-center gap-4 flex-wrap"
          >
            <a 
              href="/" 
              className="inline-flex items-center border border-terminal-green text-terminal-green hover:bg-terminal-green/10 px-4 py-2 rounded group"
            >
              <BookOpen size={16} className="mr-2 group-hover:rotate-12 transition-transform" />
              Read Docs
            </a>
            <a 
              href="https://github.com/pythonicforge/CommitPal" 
              className="inline-flex items-center bg-terminal-green hover:bg-terminal-brightGreen text-terminal-black px-4 py-2 rounded group"
            >
              <Rocket size={16} className="mr-2 group-hover:translate-x-1 transition-transform" />
              View Code
            </a>
          </motion.div>
        </motion.section>

        <section className="mb-16">
          <h2 className="text-2xl font-bold font-mono mb-6 text-terminal-green border-b border-terminal-lightGray pb-2">
            Quick Start
          </h2>
          <div className="space-y-6">
            <div>
              <h3 className="font-mono text-lg mb-2">1. Installation</h3>
              <Terminal>
                <span className="text-gray-400">$</span> git clone https://github.com/pythonicforge/CommitPal.git
              </Terminal>
            </div>
            
            <div>
              <h3 className="font-mono text-lg mb-2">2. Basic Usage</h3>
              <Terminal>
                <span className="text-gray-400">$</span> cd CommitPal<br/>
                <span className="text-gray-400">$</span> pip install -r requirements.txt<br/>
                <span className="text-gray-400">$</span> python main.py
              </Terminal>
            </div>
            
            <div>
              <h3 className="font-mono text-lg mb-2">3. With Style</h3>
              <Terminal>
                <span className="text-gray-400">$</span> diff --style=emoji
              </Terminal>
            </div>
          </div>
        </section>

        <section className="mb-16">
          <h2 className="text-2xl font-bold font-mono mb-6 text-terminal-green border-b border-terminal-lightGray pb-2">
            CLI Options
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-x-8">
            <div>
              <FlagGroup title="Style" flags={aiFlags} />
              <FlagGroup title='GitHub' flags={gitFlags}/>
            </div>
            <div>
              <FlagGroup title="Changelog" flags={changelogFlags} />
            </div>
          </div>
        </section>

        <section className="mb-16">
          <h2 className="text-2xl font-bold font-mono mb-6 text-terminal-green border-b border-terminal-lightGray pb-2">
            Example Outputs
          </h2>
          <div className="space-y-6">
            <CommitExample 
              style="conventional" 
              message="feat(auth): implement OAuth2 authentication flow
              
This adds complete OAuth2 authentication including:
- Google provider integration
- Refresh token handling
- Session management"
            />
            <CommitExample 
              style="emoji" 
              message="✨ Add user dashboard with activity graphs
              
🔧 Fix responsive layout on mobile devices
🔒 Update security dependencies"
            />
            <CommitExample 
              style="detailed" 
              message="Add caching layer to API endpoints
              
- Implemented Redis cache for user profile endpoints
- Added cache invalidation on user data updates
- Reduced average response time from 230ms to 45ms
- Added cache hit ratio metrics

Closes #234"
            />
            <CommitExample 
              style="haiku" 
              message="Fixed database bug
Connections now properly close
Memory is freed"
            />
          </div>
        </section>

        <section className="mb-16">
          <h2 className="text-2xl font-bold font-mono mb-6 text-terminal-green border-b border-terminal-lightGray pb-2">
            Why CommitPal?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div className="bg-terminal-gray p-6 rounded-lg border border-terminal-lightGray">
              <div className="mb-4 text-terminal-green">
                <Code size={28} />
              </div>
              <h3 className="font-mono text-lg mb-2">Better Commit History</h3>
              <p className="opacity-80">
                Create consistent, informative commit messages that make your git history actually useful.
              </p>
            </div>
            <div className="bg-terminal-gray p-6 rounded-lg border border-terminal-lightGray">
              <div className="mb-4 text-terminal-green">
                <TerminalIcon size={28} />
              </div>
              <h3 className="font-mono text-lg mb-2">Save Time</h3>
              <p className="opacity-80">
                Stop staring at the commit prompt. Let AI do the heavy lifting while you focus on your code.
              </p>
            </div>
            <div className="bg-terminal-gray p-6 rounded-lg border border-terminal-lightGray">
              <div className="mb-4 text-terminal-green">
                <AlertCircle size={28} />
              </div>
              <h3 className="font-mono text-lg mb-2">Never Miss Details</h3>
              <p className="opacity-80">
                CommitPal analyzes code changes to include all meaningful updates that humans might overlook.
              </p>
            </div>
          </div>
        </section>

        <section className="mb-16">
          <h2 className="text-2xl font-bold font-mono mb-6 text-terminal-green border-b border-terminal-lightGray pb-2">
            Contributing
          </h2>
          <div className="space-y-4">
            <p>
              We welcome contributions from the community! CommitPal is open source and we'd love your help.
            </p>
            <Terminal>
              <span className="text-gray-400">$</span> git clone https://github.com/pythonicforge/CommitPal.git<br/>
              <span className="text-gray-400">$</span> cd CommitPal<br/>
              <span className="text-gray-400">$</span> pip install -r requirements.txt<br/>
              <span className="text-gray-400">$</span> python main.py<br/>
              <span className="text-gray-400">$</span> # Make your changes<br/>
              <span className="text-gray-400">$</span> pytest<br/>
              <span className="text-gray-400">$</span> # Submit a PR
            </Terminal>
            <div className="flex items-center gap-4">
              <a 
                href="https://github.com/pythonicforge/CommitPal/issues" 
                target="_blank"
                rel="noopener noreferrer" 
                className="inline-flex items-center text-terminal-green hover:underline font-mono"
              >
                <span>Browse Issues</span>
                <ChevronRight size={16} />
              </a>
              <a 
                href="https://github.com/pythonicforge/CommitPal" 
                target="_blank"
                rel="noopener noreferrer" 
                className="inline-flex items-center text-terminal-green hover:underline font-mono"
              >
                <span>View Source</span>
                <ArrowRight size={16} />
              </a>
            </div>
          </div>
        </section>

        <section className="my-16 text-center">
          <div className="bg-terminal-gray p-8 rounded-lg border border-terminal-lightGray">
            <div className="inline-flex mb-4">
              <Heart className="text-terminal-green" size={28} />
            </div>
            <h2 className="text-2xl font-bold font-mono mb-4">Ready to level up your commits?</h2>
            <p className="mb-6 opacity-90 max-w-lg mx-auto">
              Start writing better commit messages today without the mental overhead.
            </p>
            <Terminal className="text-center inline-block mx-auto">
              <span className="text-gray-400">$</span> (commitpal) diff --auto-push
            </Terminal>
          </div>
        </section>
        
        <Footer />
      </div>
    </div>
  );
};

export default Index;
