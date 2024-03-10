import { Box, Container, Flex, Heading, Icon, Stack, useColorModeValue } from '@chakra-ui/react';
import { ReactElement } from 'react';
import { FaShoppingCart, FaLaptop, FaMobileAlt, FaCouch, FaTv } from 'react-icons/fa';

interface CardProps {
  heading: string;
  icon: ReactElement;
}

const Card = ({ heading, icon }: CardProps) => {
  return (
    <Box
      maxW={{ base: 'full', md: '120px' }} // Adjusted width here
      w={'full'}
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      p={2}
      bg="white"
    >
      <Stack align={'center'} spacing={2}>
        <Box
          w={8}
          h={8}
          display="flex"
          alignItems="center"
          justifyContent="center"
          color="black"
          rounded={'full'}
          bg={useColorModeValue('gray.100', 'gray.700')}
        >
          {icon}
        </Box>
        <Box mt={2}>
          <Heading size="sm" textAlign="center">{heading}</Heading> {/* Adjusted size here */}
        </Box>
      </Stack>
    </Box>
  );
};

const Category = () => {
  return (
    <Box p={4}>


      <Container maxW={'70vw'} mt={12}> {/* Adjusted width here */}
        <Flex flexWrap="nowrap" gridGap={4} justify="center" overflowX="auto"> {/* Adjusted to nowrap */}
          <Card
            heading={'Grocery'}
            icon={<Icon as={FaShoppingCart} w={6} h={6} />}
          />
          <Card
            heading={'Electronics'}
            icon={<Icon as={FaLaptop} w={6} h={6} />}
          />
          <Card
            heading={'Mobile'}
            icon={<Icon as={FaMobileAlt} w={6} h={6} />}
          />
          <Card
            heading={'Home & Furniture'}
            icon={<Icon as={FaCouch} w={6} h={6} />}
          />
          <Card
            heading={'Appliance'}
            icon={<Icon as={FaTv} w={6} h={6} />}
          />
        </Flex>
      </Container>
    </Box>
  );
};

export default Category;  