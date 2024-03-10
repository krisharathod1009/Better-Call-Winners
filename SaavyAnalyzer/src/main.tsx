import React from 'react';
import ReactDOM from 'react-dom';
import { ChakraProvider } from '@chakra-ui/react';
import Navbar from './components/Navbar';
import Footer from './components/Homepage/Footer';
import Hero from './components/Homepage/Hero';


const App = () => {
  return (
    <ChakraProvider>
        
      <Navbar />
      
    
    </ChakraProvider>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
