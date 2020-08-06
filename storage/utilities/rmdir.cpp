#include <filesystem>
#include <iostream>

int main(int argc, char const* argv[])
{
    namespace fs = std::filesystem;
    fs::remove_all(argv[1]);
    return 0;
}
