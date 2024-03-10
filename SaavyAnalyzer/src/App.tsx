import React from 'react';
import ReactDOM from 'react-dom';
import { ChakraProvider } from '@chakra-ui/react';
import Navbar from './components/Navbar';
import Footer from './components/Homepage/Footer';

const App = () => {
  return (
    <ChakraProvider>
      <Navbar />
     hii
      <Footer />
    </ChakraProvider>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
