#include <filesystem>
#include <iostream>

int main(int argc, char const* argv[])
{
    namespace fs = std::filesystem;
    std::cout << "Hello 2" << std::endl;
    // fs::create_directory(argv[1]);
    return 0;
}
