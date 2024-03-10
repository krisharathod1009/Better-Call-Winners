import { Box, Container, Text } from '@chakra-ui/react';
 // Assuming this is the path to your ProductTable component

const Resultant = () => {
  const products = [
    {
      id: 1,
      name: 'Product 1',
      description: 'Description of Product 1',
      price: '$19.99',
      imageUrl: 'https://via.placeholder.com/150x150',
    },
    // Add more products as needed
  ];

  return (
    <Container maxW="container.md" mt={4}>
      <Text fontSize="xl" fontWeight="bold" mb={4}>
        Search Results
      </Text>
     
    </Container>
  );
};

export default Resultant;
