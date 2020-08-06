#include <filesystem>
#include <iostream>

int main(int argc, char const* argv[])
{
    namespace fs = std::filesystem;
    fs::create_directory(argv[1]);
    return 0;
}
