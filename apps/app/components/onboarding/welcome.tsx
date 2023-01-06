// next
import Image from "next/image";
// icons
import Logo from "public/logo.png";

const Welcome = () => {
  return (
    <div className="h-full">
      <div className="h-1/2">
        <Image src={Logo} height={130} width={130} alt="Plane Logo" />
      </div>
      <div className="mx-auto h-1/2 space-y-4 lg:w-2/3">
        <h2 className="text-2xl font-medium">Welcome to Plane</h2>
        <p className="text-sm text-gray-400">
          Plane helps you plan your issues, cycles, and product modules to ship faster.
        </p>
        <p className="text-sm text-gray-400">1/5</p>
      </div>
    </div>
  );
};

export default Welcome;
