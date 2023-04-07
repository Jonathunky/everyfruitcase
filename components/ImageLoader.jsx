import Image from "next/image";

const ImageLoader = ({ src, alt = "", width, height }) => {
  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      objectFit="cover"
      layout="responsive"
    />
  );
};

export default ImageLoader;
