import React from 'react';
import { Box, Text, Image, Table, Tbody, Tr, Td, Center } from '@chakra-ui/react';

// Sample product data
const products = [
 {
    id: 1,
    name: 'Product 1',
    price: '$19.99',
    imageUrl: 'https://via.placeholder.com/150x250',
 },
 {
    id: 2,
    name: 'Product 2',
    price: '$29.99',
    imageUrl: 'https://via.placeholder.com/150x250',
 },
 {
    id: 3,
    name: 'Product 3',
    price: '$39.99',
    imageUrl: 'https://via.placeholder.com/150x250',
 },
 {
    id: 4,
    name: 'Product 4',
    price: '$49.99',
    imageUrl: 'https://via.placeholder.com/150x250',
 },
 {
    id: 5,
    name: 'Product 5',
    price: '$59.99',
    imageUrl: 'https://via.placeholder.com/150x250',
 },
];

const Recommend = () => {
 const productsPerRow = 5;
 const rows = Math.ceil(products.length / productsPerRow);

 const getProductAtIndex = (rowIndex: number, colIndex: number) => {
    const index = rowIndex * productsPerRow + colIndex;
    return index < products.length ? products[index] : null;
 };

 return (
    <Center h="100vh"> {/* Center the entire content vertically */}
      <Box textAlign="center" mb="4">
        <Text fontSize="xl" fontWeight="bold" mb="4">Recommended Products</Text>
        <Table variant="simple" mx="auto">
          <Tbody>
            {[...Array(rows)].map((_, rowIndex) => (
              <Tr key={rowIndex}>
                {[...Array(productsPerRow)].map((_, colIndex) => (
                 <Td key={colIndex}>
                    <Box maxW="200px" borderWidth="2px" borderRadius="lg" overflow="hidden" bg="white">
                      {getProductAtIndex(rowIndex, colIndex) && (
                        <>
                          <Image src={getProductAtIndex(rowIndex, colIndex).imageUrl} alt={getProductAtIndex(rowIndex, colIndex).name} w="150px" h="250px" objectFit="cover" />
                          <Text fontWeight="semibold" fontSize="xl" mt="2">{getProductAtIndex(rowIndex, colIndex).name}</Text>
                          <Text fontWeight="semibold" fontSize="lg" color="green.500" mt="2">{getProductAtIndex(rowIndex, colIndex).price}</Text>
                        </>
                      )}
                    </Box>
                 </Td>
                ))}
              </Tr>
            ))}
          </Tbody>
        </Table>
      </Box>
    </Center>
 );
};

export default Recommend;
