namespace csharp openservices
namespace php openservices

service CsvParser  {

   /** Get a string content and parse them as a dictionary **/
   map<string, string> parse(1: string content, 2: string delimiter);
}
