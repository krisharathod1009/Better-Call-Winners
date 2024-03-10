import React, { useState } from 'react';
import Head from 'next/head';
import { SearchIcon } from '@chakra-ui/icons';
import { InputGroup, Input, InputRightElement } from '@chakra-ui/react';
import {
  Box,
  Heading,
  Container,
  Text,
  Stack,
} from '@chakra-ui/react';
import { ReactNode } from 'react';

interface HeroProps {
  children?: ReactNode;
}

// Assuming you have a list of items to search through
const items = [
  { id: 1, name: 'Item 1' },
  { id: 2, name: 'Item 2' },
  // Add more items as needed
];

export default function Hero({ children }: HeroProps) {
  const [searchTerm, setSearchTerm] = useState('');

  // Function to filter items based on the search term
  const filteredItems = items.filter(item =>
    item.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <Head>
        <title>Call to Action with Annotation</title>
      </Head>
      <Container maxW={'3xl'}>
        <Stack
          as={Box}
          textAlign={'center'}
          spacing={{ base: 4, md: 8 }}
          py={{ base: 10, md: 20 }}>
          <Heading
            fontWeight={600}
            fontSize={{ base: '2xl', sm: '4xl', md: '6xl' }}
            lineHeight={'110%'}>
            Make money from <br />
            <Text as={'span'} color={'green.400'}>
              your audience
            </Text>
          </Heading>
          <Box>
            <InputGroup size="lg">
              <Input
                placeholder="Search"
                bg="white"
                borderRadius="full"
                fontSize="lg"
                py={6}
                px={8}
                value={searchTerm} // Bind the searchTerm state to the input value
                onChange={(e) => setSearchTerm(e.target.value)} // Update searchTerm state on input change
              />
              <InputRightElement>
                <SearchIcon color="gray.400" />
              </InputRightElement>
            </InputGroup>
          </Box>
          {/* Display filtered items */}
          <Box>
            {filteredItems.length > 0 ? (
              filteredItems.map(item => (
                <Text key={item.id}>{item.name}</Text>
              ))
            ) : (
              <Text>No items found</Text>
            )}
          </Box>
        </Stack>
      </Container>
    </>
  );
}
