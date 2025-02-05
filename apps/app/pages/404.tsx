import React from "react";

import Link from "next/link";
import type { NextPage } from "next";
import Image from "next/image";

// layouts
import DefaultLayout from "layouts/default-layout";
// ui
import { Button } from "ui";
// images
import Image404 from "public/404.svg";

const PageNotFound: NextPage = () => {
  return (
    <DefaultLayout
      meta={{
        title: "Plane - Page Not Found",
        description: "Page Not Found",
      }}
    >
      <div className="grid h-full place-items-center p-4">
        <div className="space-y-8 text-center">
          <div className="relative mx-auto h-60 w-60 lg:h-80 lg:w-80">
            <Image src={Image404} layout="fill" alt="404- Page not found" />
          </div>
          <div className="space-y-2">
            <h3 className="text-lg font-semibold">Oops! Something went wrong.</h3>
            <p className="text-sm text-gray-500">
              Lorem ipsum dolor sit amet consectetur. Fermentum augue ipsum ipsum adipiscing tempus
              diam.
            </p>
          </div>
          <Button type="button" largePadding>
            Go to Home
          </Button>
        </div>
      </div>
    </DefaultLayout>
  );
};

export default PageNotFound;
